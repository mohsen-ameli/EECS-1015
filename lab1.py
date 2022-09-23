########################################
# EECS1015- Fall 2022
# Lab 1
#
# Your name: Mohsen Ameli
# Your section: A
# Your student ID: 219705755
# Your email contact: noobmoe@my.yorku.ca
#######################################

# Please fill out your info for each lab 
from math import pi


print("---- Lab 1 ----")
print("Name: Mohsen Ameli")
print("Section A")
print("Student id: 219705755")
print("Email: noobmoe@my.yorku.ca")

# Task 1
print('\n---- Task 1: Currency converter ----')
cad = float(input("Amount in canadian dollars: "))
print(f"Amount in other currencies: ")
print(f"USD: {cad * .76}")
print(f"EUR: {cad * .75}")
print(f"NGN: {cad * 322.24}")
print(f"CNY: {cad * 5.25}")
print(f"INR: {cad * 97.14}")

# Task 2
print('\n---- Task 2: String math ----')
str1 = str(input("str1: "))
str2 = str(input("str2: "))
str3 = str(input("str3: "))
print("String concatenation:")
print(f"str1 + str2 + str3 = {str1 + str2 + str3}")
print(f"str3 + str2 + str1 = {str3 + str2 + str1}")
print(f"str2 + str1 + str3 = {str2 + str1 + str3}")
num = int(input("Input an integer: "))
print(f"num x str1 = {num * str1}")
print(f"num x str2+str3 = {num * (str2 + str3)}")


# Task 3
print("\n---- Task 3: Math operators ----")
x = int(input("Input integer x: "))
y = int(input("Input integer y: "))
print("Integer math: ")
print(f"x / y = {x/y}")
print(f"x // y = {x//y}")
print(f"x % y = {x%y}")
print(f"x ** y = {x**y}")
x = float(input("Input float x: "))
y = float(input("Input float y: "))
print("Float math: ")
print(f"x / y = {x/y}")
print(f"x // y = {x//y}")
print(f"x % y = {x%y}")
print(f"x ** y = {x**y}")


# Task 4
print('\n---- Task 4: Simple cylinder computation ----')
r = float(input("Radius: "))
h = float(input("Height: "))
print(f"Cylinder surface area: {(2 * pi * r * h) + (2 * pi * r ** 2)}")
print(f"Cylinder volume: {pi * r ** 2 * h}")


## Adding the final "input" causes python to wait on the user to press enter
## before exiting the program.
print("\n---- FINISHED ----")
input("Press enter to end.")
