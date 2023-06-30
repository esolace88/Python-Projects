import hashlib
import requests

def hash_password(password):
    sha1 = hashlib.sha1()
    sha1.update(password.encode('utf-8'))
    return sha1.hexdigest().upper()

def check_pwned(password_hash):
    prefix = password_hash[:5]
    url = f'https://api.pwnedpasswords.com/range/{prefix}'
    response = requests.get(url)

    if response.status_code == 200:
        hashes = response.text.split('\r\n')
        for hash_suffix in hashes:
            hash_suffix, count = hash_suffix.split(':')
            full_hash = prefix + hash_suffix
            if full_hash == password_hash:
                return int(count)
        return 0
    else:
        raise Exception(f"API request failed with status code {response.status_code}")

def check_password(password):
    password_hash = hash_password(password)
    count = check_pwned(password_hash)
    if count > 0:
        print(f"Your password has been found in {count} data breaches. You should change it.")
    else:
        print("Your password was not found in any data breaches. It's still a good idea to use a strong, unique password.")

if __name__ == "__main__":
    password = input("Enter your password to check if it has been hacked: ")
    check_password(password)

