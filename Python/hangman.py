import random


words = ["python", "computer", "network", "program", "keyboard"]

hangman = [
"""
 -----
 |   |
     |
     |
     |
     |
=========
""",
"""
 -----
 |   |
 O   |
     |
     |
     |
=========
""",
"""
 -----
 |   |
 O   |
 |   |
     |
     |
=========
""",
"""
 -----
 |   |
 O   |
/|   |
     |
     |
=========
""",
"""
 -----
 |   |
 O   |
/|\\  |
     |
     |
=========
""",
"""
 -----
 |   |
 O   |
/|\\  |
/    |
     |
=========
""",
"""
 -----
 |   |
 O   |
/|\\  |
/ \\  |
     |
=========
"""
]


word = random.choice(words)

guessed_letters = set()
wrong_guesses = 0
max_attempts = 6

print("Welcome to Hangman!")

while True:

   
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)


    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

  
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet.")
        continue


    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.add(guess)


    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1

        print(hangman[wrong_guesses])
        print("Wrong guess!")
        print("Attempts left:", max_attempts - wrong_guesses)

   
    if wrong_guesses == max_attempts:
        print("\nGame Over!")
        print("The word was:", word)
        break