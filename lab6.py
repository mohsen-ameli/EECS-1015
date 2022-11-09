################################
# EECS1015, York University
# Lab 6 starting code
# Name:  Mohsen Ameli
# Section:  A 
# Student ID: 219705755 
# Email:  noobmoe@my.yorku.ca
################################

from random import randrange


'''
    Task 0
'''
def task0():
    print("---- Lab 5 ----")
    print("Name: Mohsen Ameli")
    print("Section A")
    print("Student id: 219705755")
    print("Email: noobmoe@my.yorku.ca")


'''
    Task 1
'''
def average_num(*nums):
    avg = 0
    for i in nums:
        avg += i
    
    return avg / len(nums)

def task1():
    user_input = None
    loop = "Y"

    while loop == "Y":
        valid = True
        num_range = int(input("Input 4 or 5 numbers? "))

        if num_range == 4:
            user_input = str(input("Input 4 numbers [x1, x2, x3, x4] : ")).strip()
        elif num_range == 5:
            user_input = str(input("Input 5 numbers [x1, x2, x3, x4, x5] : ")).strip()
        else:
            valid = False

        if valid:
            numbers = user_input.split(",")
            numbers = list(map(int, numbers))
            
            x1 = numbers[0]
            x2 = numbers[1]
            x3 = numbers[2]
            x4 = numbers[3]
            if num_range == 5:
                x5 = numbers[4]
                avg = average_num(x1, x2, x3, x4, x5)
            else:
                avg = average_num(x1, x2, x3, x4)

            print(f"Average is {avg:.2f}")

        loop = str(input("Try again? ")).strip().upper()


'''
    Task 2
'''
def string_to_stock_dict(*astring):
    final_stock_dict = {}
    
    # Spliting stocks by a space
    for stock_dict in astring:
        stocks = stock_dict.split(" ")

        # Spliting stocks by colon
        for stock in stocks:
            stock_list = stock.split(":")
            # Filling up the final dictionary to return
            final_stock_dict[stock_list[2]] = [stock_list[0], float(stock_list[1])]

    return final_stock_dict

def print_stock_dict(stock_dict):
    keys = list(stock_dict.keys())
    print("{:10s} {:6s}  {}".format("Symbol", "Price", "Company Name"))
    print("-"*31)
    for k in keys:
        print(f"{k:7s} {stock_dict[k][1]:8.2f}   {stock_dict[k][0]}") 
        # stock_dict[k][1]
        # ^^^^^^^^^^^^^    <- this gets the list for the key k
        #              ^^^ <- this retrieves item [1] in the list (price of stock)
        #
    print() # <- an extra empty print to make it look nice

def task2():
    stock_dict1 = {"SNAP": ["Snap", 10.08], "PINS": ["Pinterest", 29.40], "GOOG": ["Google", 96.58]}
    stock_list_string = "Apple:155.74:AAPL Tesla:228.52:TSLA Ford:13.26:F Microsoft:9.12:MSFT Shopify:34.19:SHOP"
    print_stock_dict(stock_dict1)

    stock_dict2 = string_to_stock_dict(stock_list_string)
    print_stock_dict(stock_dict2)


'''
    Task 3
'''
def create_rand_list():
    num_of_element = randrange(5, 15)
    min_value = randrange(5, 10)
    max_value = randrange(20, 50)

    rand_list = []
    for i in range(num_of_element):
        rand_list.append(randrange(min_value, max_value))
    
    return rand_list

def print_list(a_list):
    print("--list--")
    if len(a_list) > 0:
        for item in a_list:
            print(f"({item})->", end="")
        print("(end)")
    else:
        print("(empty)")

def delete_item_from_list(a_list, item):
    if item in a_list:
        for i in range(len(a_list)):
            if a_list[i] == item:
                del a_list[i]
                return i
    else:
        return -1

def task3():
    delete = "Y"
    random_list = create_rand_list()

    while delete == "Y":
        # Printing the list
        print_list(random_list)

        # getting user input
        user_input = int(input("Item to delete: "))
        position = delete_item_from_list(random_list, user_input)

        # results
        if position == -1:
            print(f"Item {user_input} could not be deleted.")
        else:
            print(f"Item {user_input} successfully deleted at position {position + 1}.")
        
        # play again
        delete = str(input("Delete item [Y/N]? ")).upper()


'''
    Task 4
'''
def print_image(image):
    for line in image:
        print(line)

def uncompress_rle_image(rle_image):
    _list = []

    for step in rle_image:
        local = []
        for run in step:
            local.append(run[0] * run[1])

        string = "".join(local)
        _list.append(string)
    
    return _list

def task4():
    rle_image1 = [[(5, '-')], [(2, ' '), (1, '|')], [(2, ' '), (1, '|')], [(1, ' '), (3, '-')]]
    rle_image2 = [[(9, ' '), (1, '.'), (1, '8'), (1, '.'), (1, ' ')], [(9, ' '), (3, '8'), (1, ' ')], [(9, ' '), (3, '8'), (1, 'l')],
     [(8, ' '), (1, 'j'), (4, '8'), (1, '.')], [(7, ' '), (1, '.'), (6, '8'), (1, '.')],
     [(6, ' '), (1, '.'), (8, '8'), (1, '.')], [(4, ' '), (1, '.'), (1, 'd'), (10, '8'), (1, 'b'), (1, '.'), (1, ' ')],
     [(2, ' '), (1, '.'), (1, 'd'), (14, '8'), (1, 'b'), (1, '.')], [(1, ' '), (1, '.'), (18, '8'), (1, 'b'), (1, '.')],
     [(1, '.'), (21, '8')], [(22, '8')], [(3, '8'), (1, 'P'), (2, '"'), (1, '4'), (3, '8')],
     [(1, '`'), (1, 'P'), (1, "'"), (5, ' '), (1, '.'), (4, ' '), (1, '.'), (5, ' '), (1, '`'), (1, 'q'), (1, "'")],
     [(1, ' '), (1, '`'), (1, '-'), (2, '.'), (4, '_'), (1, ':'), (2, ' '), (1, ':'), (4, '_'), (2, '.'), (1, '-'),
      (1, "'"), (1, ' ')], [(9, ' '), (1, ':'), (2, ' '), (1, ':')], [(9, ' '), (1, ':'), (2, ' '), (1, ':')],
     [(9, ' '), (1, ':'), (2, ' '), (1, ':')], [(9, ' '), (1, ':'), (2, ' '), (1, ':')],
     [(9, ' '), (1, ':'), (2, ' '), (1, ':')],
     [(7, ' '), (1, '\\'), (1, '('), (1, '/'), (1, '\\'), (1, ')'), (1, '\\'), (1, '/'), (1, ' '), (1, 'm'), (1, 'h')]]
    rle_image3 = [[(52, '.')], [(52, '.')], [(25, '.'), (1, '/'), (1, '\\'), (25, '.')], [(18, '.'), (6, '_'), (1, '/'), (2, '_'), (1, '\\'), (7, '_'), (17, '.')], [(18, '.'), (2, '|'), (13, '-'), (2, '|'), (17, '.')], [(18, '.'), (2, '|'), (13, ' '), (2, '|'), (17, '.')], [(18, '.'), (2, '|'), (4, ' '), (1, '\\'), (3, '|'), (1, '/'), (4, ' '), (2, '|'), (17, '.')], [(18, '.'), (2, '|'), (3, ' '), (1, '['), (1, ' '), (1, '@'), (1, '-'), (1, '@'), (1, ' '), (1, ']'), (3, ' '), (2, '|'), (17, '.')], [(18, '.'), (2, '|'), (4, ' '), (1, '('), (1, ' '), (1, '.'), (1, ' '), (1, ')'), (4, ' '), (2, '|'), (7, '.'), (7, ' '), (3, '.')], [(18, '.'), (2, '|'), (4, ' '), (1, '_'), (1, '('), (1, 'O'), (1, ')'), (1, '_'), (4, ' '), (2, '|'), (7, '.'), (1, '|'), (1, 'E'), (1, 'X'), (1, 'I'), (1, 'T'), (1, ' '), (1, '|'), (3, '.')], [(18, '.'), (2, '|'), (3, ' '), (1, '/'), (1, ' '), (1, '>'), (1, '='), (1, '<'), (1, ' '), (1, '\\'), (3, ' '), (2, '|'), (7, '.'), (1, '|'), (2, '='), (2, '>'), (1, ' '), (1, '|'), (3, '.')], [(18, '.'), (2, '|'), (2, '_'), (1, '/'), (1, '_'), (1, '|'), (1, '_'), (1, ':'), (1, '_'), (1, '|'), (1, '_'), (1, '\\'), (2, '_'), (2, '|'), (17, '.')], [(18, '.'), (17, '-'), (17, '.')], [(52, '.')], [(52, '.')]]
    
    print("\t\tImage 1\n")
    image1 = uncompress_rle_image(rle_image1)
    print_image(image1)

    print("\t\tImage 2\n")
    image2 = uncompress_rle_image(rle_image2)
    print_image(image2)

    print("\t\tImage 3\n")
    image3 = uncompress_rle_image(rle_image3)
    print_image(image3)


'''
    Main
'''
def main():
    task0()
    print("\n--- Task 1: Average numbers ---")
    task1()
    print("\n--- Task 2: Text to dictionary---")
    task2()
    print("\n--- Task 3: Deleting from list---")
    task3()
    print("\n--- Task 4: RLE decoding  ---")
    task4()

    input("Press enter to end lab 6.")

if __name__ == '__main__':
    main()
