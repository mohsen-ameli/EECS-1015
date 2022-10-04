#########
# EECS1015 Fall 2022
# Lab 3
# Name: Mohsen Ameli
# Sudent id: 219705755
#########

from random import random, randrange


print("---- Lab 3 ----")
print("Name: Mohsen Ameli")
print("Section A")
print("Student id: 219705755")
print("Email: noobmoe@my.yorku.ca")


# # Task 1
# print("\n---- Task 1: Simple order ----")
# def task1():
#     price = 0
#     discount = 0

#     print("**Select menu item**")
#     print("(1) Coke [$1.00]")
#     print("(2) Dosa [$2.50]")
#     print("(3) Pizza [$2.25]")
#     print("(4) Taco [$1.50]")
#     print("(5) Tea [$1.00]")

#     selection = int(input("Selection: "))
    
#     if selection == (1 or 5):
#         price = 1
#     elif selection == 2:
#         price = 2.5
#     elif selection == 3:
#         price = 2.25
#     elif selection == 4:
#         price = 1.5
#     else:
#         print("Invalid selection - setting amount to $0")
    
#     print("**Discount**")
#     print("(C) Child [under 18] (50% discount)")
#     print("(A) Adult [18-64]")
#     print("(S) Senior [65+] (25% discount)")

#     age = str(input("Selection age: ")).upper()

#     if age == "C":
#         discount = .5
#     elif age == "S":
#         discount = .25
#     elif age == "A":
#         discount = 0
#     else:
#         discount = -.25

#     print(f"Amount    ${price:6.2f}")
#     if price != 0:
#         print(f"Discount  ${discount:6.2f}")
#     else:
#         print(f"Discount  $  0.00")
#     print("------------------")
#     print(f"Total     ${price - (discount * price):6.2f}")
# task1()


# # Task 2
# print("\n---- Task 2: Draw circle ----")
# def task2():
#     r = 0
#     while r not in range(1, 11):
#         r = int(input("Input size between 1-10: "))

#     for y in range(-10, 11):
#         for x in range(-10, 11):
#             if x**2 + y**2 <= r**2:
#                 print("*", end="")
#             else:
#                 print(".", end="")
#             if x == 10:
#                 print()
# task2()


# # task 3
# print("\n---- Task 3: Dice pair expected value ----")
# def task3():
#     again = True
#     while again:
#         N = int(input("Roll dice how many times: ")) + 1
#         avg = 0

#         for i in range(1, N):
#             rand1 = randrange(1, 7)
#             rand2 = randrange(1, 7)
#             print(f"[{rand1}]  [{rand2}] -- {(rand1 + rand2):2}   Roll {i}")
#             avg += rand1 + rand2

#         print(f"Average dice pair value: {(avg / N):4.2f}")

#         temp = str(input("Try agaian [Y/N]? ")).upper()
#         if temp == "Y":
#             again = True
#         else:
#             again = False
# task3()


# task 4
print("\n---- Task 4: Compute PI ----")
def task4():
    M = int(input("Input number of terms, M: "))
    sum = 0

    for n in range(M):
        top = (-1) ** n
        bot = (2 * n + 1)
        term = 4 * top / bot
        sum += term
        print(f"n={n} . . . adding fraction: {top}/{bot}")
        print(f"\t Our  pi = {sum:.11f}")
        print("\t real pi = 3.14159265359")
task4()

# pause program until enter is pressed
print("\n---- Lab 3 Done ----")
input("Press enter to exit.")