import random

print("Welcome to the Quiz Game!")

question1 = ["Question 1: What is the capital of France?", "A. Kyiv", "B. Paris", "C. Budapest", "D. Amsterdam", "B"]
question2 = ["Question 2: What is the capital of England?", "A. London", "B. Moscow", "C. Berlin", "D. Rome", "A"]
question3 = ["Question 3: What is the capital of Italy?", "A. Athens", "B. Copenhagen", "C. Stockholm", "D. Rome", "D"]
question4 = ["Question 4: What is the capital of Nigeria?", "A. Accra", "B. Abuja", "C. Lagos", "D. Cape Town", "B"]
question5 = ["Question 5: What is the capital of Ethiopia?", "A. Algiers", "B. Luanda", "C. Addis-Ababa", "D. Porto-Novo", "C"]

questions = [question1, question2, question3, question4, question5]

play_again = "yes"

while play_again == "yes":
    score = 0
    random.shuffle(questions)

    for question in questions:
        print()
        print(question[0])
        print(question[1])
        print(question[2])
        print(question[3])
        print(question[4])

        answer = input("Enter your option: ").upper()

        if answer == question[5]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong!, the answer was {question[5]}")

    print(f"You scored {score} points out of {len(questions)}")

    if score >= 3:
        print("You passed!")
    else:
        print("You failed. Better luck next time!")
    
    play_again = input("Do you want to play again? ").lower()

if play_again == "no":
    print("Thank you for playing, Goodbye!")