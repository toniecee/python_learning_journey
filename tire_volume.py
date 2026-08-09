#I added a feature that asks the user if they want to buy the tires.
#If they say 'yes', the program requests their phone number and appends it 
#to the volumes.txt file alongside the tire specifications.

import math
from datetime import datetime

tire_width = float(input("Input tire width in mm: "))
aspect_ratio = float(input("Input aspect ratio: "))
tire_diameter = float(input("Input tire diameter: "))

numerator = math.pi*(tire_width**2)*aspect_ratio*(tire_width*aspect_ratio+2540*tire_diameter)
denominator = 10000000000

volume = numerator/denominator

print(f"The approximate volume is {volume:.2f} liters")


to_buy = input(f"Do you want to purchase tires with {tire_width}mm width, {aspect_ratio} aspect ratio and {tire_diameter}inches diameter?(yes/no): ")

phone_number = ""

if to_buy.lower() == "yes":
    phone_number = input("Please type in your Phone Number: ")

current_date_and_time = datetime.now()
date_format = f"{current_date_and_time:%Y-%m-%d}"
with open("volumes.txt", "at") as file:
    if phone_number:
        file.write(f"{date_format}, {tire_width:.0f}, {aspect_ratio:.0f}, {tire_diameter:.0f}, {volume:.2f}, {phone_number}\n")
    else:
        file.write(f"{date_format}, {tire_width:.0f}, {aspect_ratio:.0f}, {tire_diameter:.0f}, {volume:.2f}\n")

print("Data successfully appended to volumes.txt")