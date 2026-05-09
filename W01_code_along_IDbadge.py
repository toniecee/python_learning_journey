"""
Author: Anthony Agbonoga
Purpose: Practice strings using the W01 code along activity

"""

print("Please enter the following information")

print ()

first_name = input("Enter first name: ")
first_name = first_name.title()
last_name = input("Enter last name: ")
last_name = last_name.upper()
email = input("Enter email address: ")
email = email.lower()
phone_number = input("Enter phone number: ")
job = input("Enter job title: ")
ID = input("Enter ID number: ")


print ()
print ()

print ("The ID Card is:")
print("------------------------------------------")
print (f"Name: {last_name}, {first_name}")
print (f"Email address: {email}")
print (f"Phone No.: {phone_number}")
print (f"ID: {ID}")
print("------------------------------------------")


