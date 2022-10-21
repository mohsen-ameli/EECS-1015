################################
# EECS1015, York University
# Lab 5 starting code
# Name:  Mohsen Ameli
# Section:  A 
# Student ID: 219705755 
# Email:  noobmoe@my.yorku.ca
################################

# Print info
def print_lab_info():
    print("---- Lab 5 ----")
    print("Name: Mohsen Ameli")
    print("Section A")
    print("Student id: 219705755")
    print("Email: noobmoe@my.yorku.ca")


def task0():
  # Example of calling a function from taskX() functions.
  # you should write all functions "outside" your task1()-task4() functions.
  print_lab_info()

def input_list():
  stop = False
  list_ = []

  while not stop:
    user_input = int(input("Input positive int: "))
    if user_input >= 0 :
      list_.append(user_input)
    else:
      stop = True
  
  return list_

def compute_average(list_):
  total = 0

  for i in range(len(list_)):
    total += list_[i]
  
  if len(list_) > 0:
    return total / len(list_)
  else:
    return 0

def task1():
  repeat = True

  while repeat:
    computed_list = input_list()
    avg = compute_average(computed_list)
    
    print(f"List average {avg:.2f}")

    again = str(input("Again [Y/N]? ")).lower()

    if again != "y":
      repeat = False

def task2():
  star = "*"

  long_str = str(input("Input a long string: ")).upper()

  # Converting to a list
  list_ = list(long_str)

  # Converting to a set
  set_ = set(long_str)

  # Converting to a dictionary
  dict_ = {}
  for item in set_:
    dict_[item] = 0

  for item in list_:
    dict_[item] += 1

  for key, value in dict_.items():
    print(f"'{key}'  |{star * value}")
    
def task3():
  encoder = {'A': '$', 'B': 'F', 'C': 'C', 'D': '2', 'E': 'B', 'F': 'I', 'G': '=', 'H': '*', 'I': '"', 'J': ']', 'K': '1',
     'L': '0', 'M': '@', 'N': '[', 'O': 'L', 'P': '%', 'Q': '&', 'R': '(', 'S': 'G', 'T': 'K', 'U': '5', 'V': '!',
     'W': '^', 'X': '+', 'Y': '6', 'Z': '-', '1': 'H', '2': 'A', '3': 'J', '4': '7', '5': '4', '6': 'D', '7': 'E',
     '8': '9', '9': ')', '0': ';', ',': '3', '.': '/', ' ':'_'}
  decoder = {'$': 'A', 'F': 'B', 'C': 'C', '2': 'D', 'B': 'E', 'I': 'F', '=': 'G', '*': 'H', '"': 'I', ']': 'J', '1': 'K',
     '0': 'L', '@': 'M', '[': 'N', 'L': 'O', '%': 'P', '&': 'Q', '(': 'R', 'G': 'S', 'K': 'T', '5': 'U', '!': 'V',
     '^': 'W', '+': 'X', '6': 'Y', '-': 'Z', 'H': '1', 'A': '2', 'J': '3', '7': '4', '4': '5', 'D': '6', 'E': '7',
     '9': '8', ')': '9', ';': '0', '3': ',', '/': '.', '_': ' '}

def task4():
  pass


def main():
    ### Don't forget to update print_lab_info() function
    task0()

    print("\n---- Task 1: List average ----")
    # task1()

    print("\n---- Task 2: Character count graph ----")
    task2()

    print("\n---- Task 3: Encoder/decoder ----")
    task3()

    print("\n---- Task 4: Lotto LESS ----")
    task4()

if __name__ == "__main__":
    main()