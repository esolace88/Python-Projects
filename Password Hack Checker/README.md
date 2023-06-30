# Password Hack Checker

Welcome to the Password Hack Checker project! This project is a Python script that checks whether a password has been exposed in a data breach.

## Getting Started

To get started, you will need Python installed on your machine. If you haven't installed Python yet, you can download it from the official website: https://www.python.org/downloads/

Once you have Python installed, you can clone the repository and navigate to the Password Hack Checker directory as follows:

```bash
git clone https://github.com/esolace88/Python-Projects.git
cd Python-Projects/Password\ Hack\ Checker
```

To start the password check, run the following command:

```bash
python hack_checker.py
```

## How it Works

This script uses the 'Have I Been Pwned' API to check whether a password has been exposed in a data breach. You enter your password, and the script will tell you whether it has been exposed and how many times.

## Code Explanation

The Password Hack Checker is composed of a few functions.

- `request_api_data(query_char)`: This function requests data from the 'Have I Been Pwned' API. The API uses a k-anonymity model, which allows a password to be checked without sending the entire password to the service.

- `get_password_leaks_count(hashes, hash_to_check)`: This function receives a hash response and checks whether our password is in this response. It returns the number of times the password has been leaked.

- `pwned_api_check(password)`: This function hashes the password using SHA1 and uses only the first 5 characters of this hash to get a response from the API. This is in line with the k-anonymity model.

- `main(args)`: This is the main function that reads password(s) from the command line and checks each one.

The script uses the `requests` and `hashlib` libraries. You will need to install the requests library if it's not already installed. You can do this using pip:

```bash
pip install requests
```

## Contributing

If you'd like to contribute, feel free to open a pull request or issue. All contributions are welcome!

Stay safe and secure with your passwords!
