grade = float(input("Input your grade percent: "))

if grade >= 90:
    point = "A"
elif grade >= 80:
    point = "B"
elif grade >= 70:
    point = "C"
elif grade >= 60:
    point = "D"
else:
    point = "F"

if point[0].lower() in "aeiouf":
    article = "an"
else:
    article = "a"

last_digit = grade % 10
if last_digit >=7:
    sign = "+"
elif last_digit < 3:
    sign = "-"
else:
    sign = ""


if point == "A" and sign == "+":
    sign = ""
if point == "F" and (sign == "+" or sign == "-"):
    sign = ""
print()
print(f"You have earned {article} {point}{sign}.")
print()
if grade >= 70:
    print("Congratulations, you have passed the course.")
else:
    print("Sorry, but you have failed the course.")
print()