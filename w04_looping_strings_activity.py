word = input("What is your favourite word? ")
user_letter = input("What is your favourite letter in the word? ")

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