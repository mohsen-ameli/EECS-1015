#########
# EECS1015 Fall 2022
# Lab 2
# Name: Mohsen Ameli
# Sudent id: 219705755
#########

print("---- Lab 2 ----")
print("Name: Mohsen Ameli")
print("Section A")
print("Student id: 219705755")
print("Email: noobmoe@my.yorku.ca")

# Task 1
print("\n---- Task 1: Three year investment return ----")
def task1():
    name = str(input("Name: ")).strip()
    initial = float(input("Initial amount: $ "))
    rate = int(input("Rate of return: % "))
    print(f"Client: {name.title()}, yearly rate of return multiplier: {(rate / 100):.2f}")
    multiplier = initial + (initial * (rate / 100))
    print(f"Year 1 \t Starting Amount: ${initial:8.2f} \t\t Ending Amount: ${multiplier:8.2f}")
    multiplier2 = multiplier + (multiplier * (rate / 100))
    print(f"Year 2 \t Starting Amount: ${multiplier:8.2f} \t\t Ending Amount: ${multiplier2:8.2f}")
    multiplier3 = multiplier2 + (multiplier2 * (rate / 100))
    print(f"Year 3 \t Starting Amount: ${multiplier2:8.2f} \t\t Ending Amount: ${multiplier3:8.2f}")
task1()


# Task 2
print("\n----Task 2 Leetspeak converter ----")
def task2():
    long_str = str(input("Type a long string: ")).upper()
    formatted_str = long_str.replace("T", "7").replace("A", "^").replace("E", "3").replace("I", "!").replace("B", "8").replace("O", ".").replace("C", "<").replace("S", "$")
    print(formatted_str)
task2()

# task 3
print("\n---- Task 3: Substring highlighter ----")
def task3():
    print("Type a sentence at the prompt below:")
    long_str = str(input("> "))
    print("Enter substring below to highlight:")
    sub_str = str(input("> "))
    print(f"Sentence has {len(long_str)} characters, substring has {len(sub_str)} characters.")
    
    firstIndex = long_str.find(sub_str)
    lastIndex = firstIndex + len(sub_str)
    sliced = slice(firstIndex, lastIndex)
    print("Substring highlighted:")
    print(f"> {long_str[:firstIndex]}*{long_str[sliced].upper()}*{long_str[lastIndex:]}")
task3()

# task 4
print("\n---- Task 4: Exponent ----")
def task4():
    string = str(input("Input exponent in the form x^y: "))
    num1 = int(string.split("^")[0])
    num2 = int(string.split("^")[1])
    print(f"Extracted numbers {num1} {num2}")
    print(f"{num1}^{num2} = {num1 ** num2}")
task4()

# pause program until enter is pressed
print("\n---- Lab 2 Done ----")
input("Press enter to exit.")