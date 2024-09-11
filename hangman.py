import random

def get_word():
    words = ['mango','guava','apple','watermelon','orange','pineapple']
    return random.choice(words)

def display_board(word, guessed_letters):
    display_word = [letter if letter in guessed_letters else '_' for letter in word]
    print(' '.join(display_word))

def play_hangman():
    word = get_word()
    guessed_letters = []
    attempts = 6
    print("Welcome to Hangman!")
    
    while attempts > 0:
        display_board(word, guessed_letters)
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
        elif guess in word:
            guessed_letters.append(guess)
            print(f"Good guess! '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"Wrong guess. You have {attempts} attempts left.")
            guessed_letters.append(guess)

        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You've guessed the word '{word}'!")
            break
    else:
        print(f"Game over! The word was '{word}'.")

play_hangman()
