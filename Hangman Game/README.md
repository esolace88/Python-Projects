# Hangman Game

Welcome to the Hangman Game project! This is a simple, text-based game of hangman implemented in Python.

## Getting Started

To get started, you will need Python installed on your machine. If you haven't installed Python yet, you can download it from the official website: https://www.python.org/downloads/

Once you have Python installed, you can clone the repository and navigate to the Hangman Game directory as follows:

```bash
git clone https://github.com/esolace88/Python-Projects.git
cd Python-Projects/Hangman\ Game
```

To start the game, run the following command:

```bash
python hangman.py
```

## Game Rules

The rules of Hangman are simple:

1. The computer randomly selects a word.
2. The player guesses one letter at a time.
3. If the letter is in the word, the computer fills in the blanks with the correctly guessed letters.
4. If the letter is not in the word, the player loses a life.
5. The player continues guessing letters until they either guess the word correctly or run out of lives.

## Code Explanation

The Hangman game is a simple Python script composed of a few functions.

- `get_word()`: This function selects a random word from a predefined list of words. This is the word that the player will try to guess.

- `play_hangman()`: This function manages the game logic. It repeatedly asks the user for a letter, checks if the letter is in the word, and updates the guessed letters and remaining lives accordingly.

- `print_word_to_guess()`: This function prints out the current state of the word to guess, with underscores for unguessed letters and the actual letter for correctly guessed letters.

- `print_lives()`: This function prints out the number of lives remaining in a visually pleasing manner.

The code uses standard Python libraries, so no extra installations are necessary. It's a great project for beginners looking to practice their Python skills.

## Contributing

If you'd like to contribute, feel free to open a pull request or issue. All contributions are welcome!

Happy guessing and enjoy the game!

