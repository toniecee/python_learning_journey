import random

play_again = "yes"

guess = -1
guess_count = 0
user_num = random.randint(1, 200)

while play_again == "yes":
    user_num = random.randint(1, 100)
    guess_count = 0
    guess = -1
    while guess != user_num:
        guess = int(input("What is your guess? "))
        guess_count = guess_count + 1
        if guess > user_num:
            print("lower")
        elif guess < user_num:
            print("higher")
        else:
            print("you guessed it!")

    if guess_count > 1:
        print(f"It took you {guess_count} guesses")
    else:
        print(f"It took you {guess_count} guess.")

    play_again = input("Would you like to play again (yes/no)? ")
print("Thank you for playing. Goodbye!")