import math

# I have added a tip percentage to the total amount
child_meal = float(input("input price of child meal ($): "))
adult_meal = float(input("input price of adult meal ($): "))
num_children = int(input("input total number of children: "))
num_adults = int(input("input total number of adults: "))
subtotal = (child_meal * num_children) + (adult_meal * num_adults)
print()
print(f"Subtotal: ${subtotal: .2f}")
print()
tax_rate = float(input("input tax ($): "))
sales_tax = (subtotal * tax_rate) / 100
tip_rate = float(input("input tip ($): "))
tip_percent = (subtotal * tip_rate) / 100
total = subtotal + sales_tax + tip_percent
print()
print(f"Total: ${total: .2f}")
print()
payment = float(input("What is the payment amount ($)? "))
change = payment - total
print(f"Change: ${change: .2f}")