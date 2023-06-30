import random

def choose_word():
    words = {
        'apple': 'A common fruit, usually red or green',
        'banana': 'A long, curved, yellow fruit',
        'cherry': 'A small, round, red fruit',
        'dragonfruit': 'An exotic fruit with a white interior and black seeds',
        'elderberry': 'A dark purple berry used in syrups and jams',
        'fig': 'A small, pear-shaped fruit with a soft, sweet interior',
        'grape': 'A small, round, green or purple fruit often used to make wine',
        'honeydew': 'A green melon with a pale green, sweet interior',
        'kiwi': 'A fuzzy, brown fruit with a green interior and black seeds',
        'lemon': 'A sour, yellow citrus fruit',
        'mango': 'A tropical fruit with a large pit and sweet, juicy flesh',
        'nectarine': 'A smooth-skinned relative of the peach',
        'orange': 'A round, sweet, orange citrus fruit',
        'papaya': 'A tropical fruit with a sweet, orange flesh',
        'quince': 'A yellow, pear-shaped fruit often used in jams and jellies',
        'raspberry': 'A small, red, sweet, and tart berry',
        'strawberry': 'A red, heart-shaped fruit with tiny seeds on the surface',
        'tangerine': 'A small, sweet, orange citrus fruit',
        'ugli': 'A citrus fruit with a wrinkled, greenish-yellow rind',
        'vanilla': 'A flavor derived from the pod of an orchid',
        'watermelon': 'A large, green fruit with a sweet, red or yellow interior',
        'xigua': 'A Chinese term for a type of watermelon',
        'yellowpassion': 'A type of passion fruit with a yellow rind',
        'zucchini': 'A green summer squash'
    }
    return random.choice(list(words.items()))

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def play_hangman():
    word, description = choose_word()
    guessed_letters = set()
    attempts_remaining = 6
    print(f"Welcome to Hangman! You have {attempts_remaining} attempts to guess the word.")
    print(f"Hint: {description}")

    while attempts_remaining > 0:
        print(display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please guess a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed this letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct guess!")
        else:
            attempts_remaining -= 1
            print(f"Incorrect guess. You have {attempts_remaining} attempts remaining.")

        if set(word).issubset(guessed_letters):
            print(f"Congratulations! You've guessed the word: {word}")
            break
    else:
        print(f"Game over. The word was: {word}")

if __name__ == "__main__":
    play_hangman()

