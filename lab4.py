################################
# EECS1015 York Univresity
# Lab 4 - Starter Code
# Name: Mohsen Ameli
# Section A
# Student id: 219705755
# Email: noobmoe@my.yorku.ca
################################

from random import randrange
from time import sleep

num_of_jumps = None

eye1 = '{o,o}'
eye2 = '{-,o}'
eye3 = '{o,-}'
body = '/)_) '
feet = ' " " '

frame1 = "  o   \n /|\  \n / \  "
frame2 = " \o/  \n  |   \n / \  "


def print_student_info():
    print("Name: Mohsen Ameli")
    print("Section A")
    print("Student id: 219705755")
    print("Email: noobmoe@my.yorku.ca")

def get_input(prompt, min, max, int_or_float):
    while True:
        if int_or_float == "int":
            user_input = int(input(prompt))
        else:
            user_input = float(input(prompt))
        if user_input >= min and user_input <= max:
            return user_input

def get_yes(prompt):
    while True:
        user_input = str(input(prompt)).upper()
        if user_input == "Y":
            return True
        elif user_input == "N":
            return False

def draw_owl(position, randomize=False):
    # Movement
    spaces = " " * position

    # Owl head
    if randomize:
        rand = randrange(1, 4)
        if rand == 1:
            print(f"{spaces}{eye1}")
        elif rand == 2:
            print(f"{spaces}{eye2}")
        elif rand == 3:
            print(f"{spaces}{eye3}")
    else:
        print(f"{spaces}{eye1}")

    # Rest of owl
    print(f"{spaces}{body} \n{spaces}{feet}")

def compute_return(amount, rate, years):
    new_amount = amount

    for i in range(int(years)):
        new_amount = new_amount + (new_amount * rate)
    
    return new_amount

def task1():
    N = (get_input("How many times to move [2-20]? ", 2, 20, "int"))
    T = get_input("How long to delay [1-1000ms]? ", 1, 1000, "int")
    randomize = get_yes("Randomize [Y/N]? ")

    for i in range(N):
        draw_owl(i, randomize)
        sleep(T/1000)

def task2():
    again = True

    while again:
        amount = get_input("Input initial investment amount [1, 10000]? ", 1, 10000, "float")
        rate = get_input("Annual return rate [0-1]? ", 0, 1, "float")
        years = get_input("How many years [1-10]? ", 1, 10, "int")

        return_value = compute_return(amount, rate, years)

        if years == 1:
            print(f"Return in {years} year is: ${return_value:10.2f}")
        else:
            print(f"Return in {years} years is: ${return_value:10.2f}")

        again = get_yes("Compute new investment [Y/N]? ")

def task3():
    max = 1
    for i in range(4):
        odd = get_input(f"[{i + 1}/5]\tEnter a number [1-100]: ", 1, 100, "int")
        if odd % 2 != 0:
            if max < odd:
                max = odd
    print(f"Final max odd number: {max}.")

    global num_of_jumps
    num_of_jumps = max

def task4():
    input(f"Press enter to perform {num_of_jumps} jumping jacks.")

    for i in range(num_of_jumps):
        if i % 2 == 0:
            for a in frame2.split("\n"):
                if a == ' \\o/  ':
                    print(f"{a} [  {i+1}]")
                else:
                    print(a)
        else:
            for a in frame1.split("\n"):
                if a == '  o   ':
                    print(f"{a} [  {i+1}]")
                else:
                    print(a)

def main():
    print_student_info()

    print("\n---- Task 1: The Owl ----")
    task1()
    print("\n---- Task 2: Compound investment ---")
    task2()
    print("\n---- Task 3: Max odd number ----")
    task3()
    print("\n---- Task 4: Jumping Jacks ----")
    task4()
    input("Press enter to end lab 4.")

if __name__ == "__main__":
    main()