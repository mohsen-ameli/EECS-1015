################################
# EECS1015, York University
# Lab 5 starting code
# Name:  Mohsen Ameli
# Section:  A 
# Student ID: 219705755 
# Email:  noobmoe@my.yorku.ca
################################

# Print info
from random import randint


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
  again = "Y"

  while again == "Y":
    user_str = str(input("Input message: ")).upper()
    encode_or_decode = str(input("Encode (E) or Decode (D)? ")).upper()

    if encode_or_decode == "E":
      encoded = []
      print("Encoded message: ")

      # Filling up encoded
      for char in user_str:
        if char in encoder:
          encoded += encoder[char]
        else:
          encoded = ""
          break

      # If encoded is empty
      if encoded == "":
        print("Invalid input")
      else:
        encoded = "".join(encoded)
        print(encoded)
    else:
      decoded = []
      print("Decoded message: ")

      for char in user_str:
        if char in decoder:
          decoded += decoder[char]
        else:
          decoded = ""
          break

      if decoded == "":
        print("Invalid input")
      else:
        decoded = "".join(decoded)
        print(decoded)
    
    again = str(input("Encode/decode again [Y/N]? ")).upper()

def random_set():
  r = set()
  i = 0

  while i in range(5):
    rand = randint(1, 20)
    if rand not in r:
      r.add(rand)
      i += 1

  return r
  
def print_set(aSet, prompt=""):
  print(prompt, end="")
  for item in aSet:
    print(item, end=" ")

def task4():
  again = "Y"

  while again == "Y":
    num_again = True
    user_guess = set()
    correct_guess = set()

    while num_again:
      # getting user's input
      user_input = str(input("Enter 5 numbers between 1-20: ")).strip()

      # splitting user's input by spaces
      num_list = user_input.split(" ")

      # converting user's input to a numbered list
      num_list = list(map(int, num_list))

      # updating our set for user's guess
      user_guess = set(num_list)
      
      # if user inputed the wrong values
      input_len = len(user_guess)
      if input_len == 5:
        num_again = False

      for num in user_guess:
        if num not in range(1, 21):
          num_again = True

    # generate computer's numbers
    aSet = random_set()
    print_set(aSet, prompt="Computer's numbers: ")

    print()

    # checking to see if user got any correct guesses
    for num in aSet:
      if num in user_guess:
        correct_guess.add(str(num))

    # printing results
    if len(correct_guess) > 0:
      print(f"{len(correct_guess)} matches found:", " ".join(correct_guess))
    else:
      print("No matches haha!")

    again = str(input("Try again [Y/N]? ")).upper()


def main():
    ### Don't forget to update print_lab_info() function
    task0()

    print("\n---- Task 1: List average ----")
    task1()

    print("\n---- Task 2: Character count graph ----")
    task2()

    print("\n---- Task 3: Encoder/decoder ----")
    task3()

    print("\n---- Task 4: Lotto LESS ----")
    task4()

if __name__ == "__main__":
    main()