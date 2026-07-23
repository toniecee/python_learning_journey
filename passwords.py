# Enhancement: I Added a visual password strength meter that displays the password's
# strength as a bar (e.g., [###--] 3/5) after each password is tested,
# making the results easier for users to understand at a glance.

LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\","`", "~"]


def main():
    while True:
        password = input("Please enter a password to test (or 'q' to quit): ")
        if password.lower() == 'q':
            print("Goodbye")
            break
        else:
            strength = password_strength(password)
            display_strength_meter(strength)

def word_in_file(word, filename, case_sensitive=False):
    with open (filename, "r", encoding="utf-8") as file:
        for line in file:
            clean_line = line.strip()
            if case_sensitive:
                if word == clean_line:
                    return True
            else:
                if word.lower() == clean_line.lower():
                    return True
    return False

def word_has_character(word, character_list):
    for character in word:
        if character in character_list:
            return True
    return False

def word_complexity(word):
    score = 0
    if word_has_character(word, LOWER):
        score += 1
    if word_has_character(word, UPPER):
        score += 1
    if word_has_character(word, DIGITS):
        score += 1
    if word_has_character(word,SPECIAL):
        score += 1
    return score

def password_strength(password, min_length = 10, strong_length = 16):
    if word_in_file(password, "wordlist.txt", case_sensitive= False):
        print("Password is a dictionary word and is not secure.")
        return 0
    if word_in_file(password, "toppasswords.txt", case_sensitive= True):
        print("Password is a commonly used password and is not secure.")
        return 0
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1
    if len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5
    complexity = word_complexity(password)
    strength = 1 + complexity
    return strength

def display_strength_meter(strength):
    filled = "#" * strength
    empty = "-" * (5 - strength)
    bar = "[" + filled + empty + "]"
    print(f"Strength: {bar} {strength}/5")


if __name__ == "__main__":
    main()