# Creativity requirement:
# I added a third list to track and display item quantities, 
# and updated the code to factor in those quantities.

#Author: Anthony Agbonoga

items = []
prices = []
quantities = []
action = ""
item_name = ""
price = ""


print("Welcome to the Shopping Cart Program!")
print()

while action != "5":
    print("Please select one of the following: ")
    print ("""1. Add item
2. View cart
3. Remove item    
4. Compute total
5. Quit""")
    print()
    action = input("Please enter an action: ")

    if action == "1":
        item_name = input("What item would you like to add? ")
        price = float(input(f"What is the price of '{item_name}'? "))
        quantity = int(input(f"How many '{item_name}' would you like to add? "))
        items.append(item_name)
        prices.append(price)
        quantities.append(quantity)
        print(f"'{item_name}' has been added to the cart.")

        print()

    elif action == "2":
        if len(items) == 0:
            print("Your cart is empty!")
        else:
            print("The contents of the shopping cart are: ")
            for i in range(len(items)):
                print(f"{i + 1}. {items[i]} (x{quantities[i]}) - ${prices[i] * quantities[i]:.2f}")

        print()

    elif action == "3":
        if len(items) == 0:
            print("Your cart is empty!")
        else:
            print("The contents of the shopping cart are: ")
            for i in range(len(items)):
                print(f"{i + 1}. {items[i]} - ${prices[i]:.2f}")

            remove_index = int(input("Which item would you like to remove? "))
            actual_index = remove_index - 1

            if actual_index >= 0 and actual_index < len(items):
                items.pop(actual_index)
                prices.pop(actual_index)
                quantities.pop(actual_index)
                print("Item removed.")
            else:
                print("Sorry, that is not a valid item number.")

        print()

    elif action == "4":
        if len(items) == 0:
            print("Your cart is empty!")
        else:
            total = 0
            for i in range(len(items)):
                total += prices[i] * quantities[i]
            print(f"The total price of the items in the shopping cart is ${total:.2f}")

        print()

    elif action == "5":
        print("Thank you. Goodbye.")
    else:
        print("Invalid action")