#I have added another adjective to the story, I also added an if-else logic to add an 'a' or 'an' in front of the second adjective. This is the 'article' variable.

"""
Author: Anthony Agbonoga
Purpose: Week 1 project
"""

print("Please enter the following information:")

adjective_1 = input("enter first adjective: ")
animal = input("enter animal name: ")
verb_1 = input("enter first verb: ")
exclamation = input("enter exclamation: ")
exclamation = exclamation.capitalize()
verb_2 = input("enter second verb: ")
verb_3 = input("enter third verb: ")
adjective_2 = input("enter second adjective: ")
if adjective_2[0].lower() in "aeiou":
    article = "an"
else:
    article = "a"


print()
print("Your story is:")
print(f"""
The other day, I was really in trouble. It all started when I saw a very
{adjective_1} {animal} {verb_1} down the hallway. '{exclamation}!' I yelled.
But all
I could think to do was to {verb_2} over and over. Miraculously,
that caused it to stop, but not before it tried to {verb_3}
right in front of my family.
This action startled everyone and they all shared {article} {adjective_2} moment.
""")