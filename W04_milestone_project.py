# I added a play again feature and a random word selector that
# picks a secret word from a list, making each game unique.

import random

play_again = "yes"

words = ["money", "brain", "plant", "cloud", "happy"]
while play_again == "yes":

    print("Welcome to the word guessing game!")

    hint = ""
    secret_word = random.choice(words)
    for i in secret_word:
        hint += "_ "
    print("Your hint is: " + hint)

    new_hint = ""

    guess_count = 0
    guess = ""
    while guess != secret_word:
        guess = input("What is your guess? ")
        guess_count = guess_count + 1
        if len(guess) != len(secret_word):
            print("Sorry, the guess must have the same number of letters as the secret word.")
        else:
            for i in range (len(secret_word)):
                if guess[i] == secret_word[i]:
                    new_hint += guess[i].upper() + " "
                elif guess[i] in secret_word:
                    new_hint += guess[i].lower() + " "
                else:
                    new_hint += "_ "
            print("Your hint is: " + new_hint)
            new_hint = ""
    
    print("Congratulations! You guessed it!")

    if guess_count > 1:
        print(f"It took you {guess_count} guesses.")
    else:
        print(f"It took you {guess_count} guess.")
    
    play_again = input("Would you like to play again (yes/no)? ").lower()
print("Thank you for playing. Goodbye!")