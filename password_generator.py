import random

print("Welcome to the password generator")
print()
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()/?"

pool = ""
new_password = "yes"


while new_password == "yes":
    pool = letters
    password_length = int(input("How long do you want your password? "))
    password_numbers = (input("Do you want numbers in your password? ")).lower()
    password_symbols = (input("Do you want symbols in your password? ")).lower()

    if password_length <= 0:
        print("Invalid length, password must be minimum 8 characters.")
        continue

    if password_numbers == "yes":
        pool += numbers

    if password_symbols == "yes":
        pool += symbols

    password = ""

    for i in range(password_length):
        password += random.choice(pool)

    print(f"Your password is {password}")
    new_password = input("Do you want to generate another password? ").lower()
print()


if new_password == "no":
    print("Thank you for using the password generator. Goodbye!")
