print("Please enter the items of the shopping list (type: quit to finish):")

shopping_list = []
item = ""

while item != "quit":
    item = input("Item: ")

    if item != "quit":
        shopping_list.append(item)

print()

print("The shopping list is:")
for item in shopping_list:
    print(f"{item}")

print()

print("The shopping list with index is:")
for i in range(len(shopping_list)):
    item = shopping_list[i]
    print(f"{i}. {item}")

print()

index = int(input("Which item would you like to change? "))
new_item = input("What is the new item? ")
shopping_list[index] = new_item

print("The shopping list with index is:")
for i in range(len(shopping_list)):
    item = shopping_list[i]
    print(f"{i}. {item}")