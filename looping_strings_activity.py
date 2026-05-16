# Creativity Addition: I modified the program to ask the user for a custom word instead of using the hardcoded word "Commitment".
"""
Author: Anthony Agbonoga
Purpose: Capitalizes letters in a string.
"""

word = input("What is your favourite word? ")
user_letter = input("What is your favourite letter? ")

for letter in word:
    if letter.lower() == user_letter.lower():
        print(letter.upper(), end="")
    else:
        print(letter.lower(), end="")
print()

for letter in word:
    if letter.lower() == user_letter.lower():
        print("_", end="")
    else:
        print(letter.lower(), end="")