import math



square_len = float(input("What is the length of a side of the square (in cm)? "))
square_area = square_len ** 2
square_area_in_meters = square_area/10000
print(f"The area of the square in cm is: {square_area: .2f}cm^2")
print(f"The area of the square in m is: {square_area_in_meters:.4f}m^2")

print()
rect_len = float(input("What is the length of the rectangle? "))
rect_width = float(input("What is the width of the rectangle? "))
rect_area = rect_len * rect_width
rect_area_in_meters = rect_area/10000
print(f"The area of the rectangle in cm is: {rect_area: .2f}cm^2")
print(f"The area of the rectangle in m is: {rect_area_in_meters:.4f}m^2")
print()
radius = float(input("What is the radius of the circle? "))
circle_area = math.pi * (radius ** 2)
circle_area_in_meters = circle_area/10000
print(f"The area of the circle in cm is: {circle_area: .2f}cm^2")
print(f"The area of the circle in m is: {circle_area_in_meters: .4f}m^2")