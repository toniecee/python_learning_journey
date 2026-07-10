from datetime import datetime
discount_rate = 10/100
tax_rate = 6/100

today = datetime.now()
day = today.weekday()

subtotal = 0
quantity = 1
while quantity != 0:
    quantity = int(input("What is the quantity? "))
    print("enter '0' when done")
    if quantity != 0:
        price = float(input("What is the price? "))
        subtotal = quantity * price

print(f"Total order: ${subtotal:.2f}")
discount = 0
if day == 1 or day == 2 or day == 4:
    if subtotal > 50:
        discount = round(subtotal * discount_rate, 2)
        print(f"Discount: {discount:.2f}")
    else:
        short = 50 - subtotal
        print(f"Spend ${short:.2f} more and get a 10% discount.")

tax = subtotal * tax_rate
print(f"Tax: ${tax:.2f}")
subtotal -= discount
total = subtotal + tax

print(f"To be paid: ${total}")

