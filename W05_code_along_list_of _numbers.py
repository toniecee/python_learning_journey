print("Enter a list of numbers, type 0 when finished.")

numbers = []
user_num = -1

while user_num != 0:
    user_num = 5
    
    if user_num != 0:
        numbers.append(user_num)

sum = 0

for user_num in numbers:
    sum = sum + user_num

average = sum/len(numbers)

largest = numbers[0]

for user_num in numbers:
    if user_num > largest:
        largest = user_num

smallest = float("inf")

for user_num in numbers:
    if user_num > 0 and user_num < smallest:
        smallest = user_num

print(f"The sum is: {sum}")
print(f"The average is: {average}")
print(f"The largest number is: {largest}")
print(f"The smallest positive number is: {smallest}")