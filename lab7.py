##################################
# EECS1015 - York University
# Author: Michael S. Brown 
# (c) MS Brown. This code cannot be shared without permission from the
# author.
# Lab 7 starter code
#
##################################


'''
    Task 0
'''
def print_student_info():
    print("---- Lab 7 ----")
    print("Name: Mohsen Ameli")
    print("Section A")
    print("Student id: 219705755")
    print("Email: noobmoe@my.yorku.ca")

def task0():
    print_student_info()


'''
    Task 1
'''
def is_sorted(a_list):
    _sorted =  sorted(a_list)
    if _sorted == a_list:
        return True
    else:
        return False

def task1():
    x1 = [1, 4, 5, 9, 0, 8, 10]
    x2 = [1, 2, 4, 5, 6, 7, 9]
    x3 = []

    print(is_sorted(x1))
    print(is_sorted(x2))
    print(is_sorted(x3))

'''
    Task 2
'''
def merge_dict(dict1, dict2):
    for key, value in dict2.items():
        if key not in dict1.keys():
            dict1.update({key: value})

def task2():
    dict1 = {8:"Exercise", 9:"Breakfast", 12:"Lunch", 3:"Study", 6:"Netflix"}
    dict2 = {8:"Sleep", 10:"Lab", 12:"Class", 4:"Call Mom"}

    print(dict1)
    print(dict2)
    merge_dict(dict1, dict2)
    print(dict1)


'''
    Task 3
'''
def invert_dict(a_dict):
    new_dict = {}

    for key, value in a_dict.items():
        new_dict.update({value: key})
    
    return new_dict

def task3():
    a_dict = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five'}

    print(a_dict)
    new_dict = invert_dict(a_dict)
    print(new_dict)


'''
    Task 4
'''
def list_to_dict(a_list):
    new_dict = {}

    for i in range(len(a_list)):
        new_dict.update({i: a_list[i]})
    
    return new_dict

def task4():
    my_list = [1, "hello", 9.99, ["EECS", "1015"], {1:"1", 2:"2"}]
    
    print(my_list)
    new_dict = list_to_dict(my_list)
    print(new_dict)

'''
    Task 5
'''
def str_list_to_num_list(a_list):
    # new_list = []

    # for i in range(len(a_list)):
    #     new_list.append(int(a_list[i]))

    return list(map(int, a_list))

def task5():
    x = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    print(x)
    new_list = str_list_to_num_list(x)
    print(new_list)
    
'''
    Task 6
'''
def merge_lists(list1, list2):
    assert sorted(list1) == list1, "List 1 is not sorted!"
    assert sorted(list2) == list2, "List 2 is not sorted!"

    final_list = []
    len1 = len(list1)
    len2 = len(list2)
    pos1 = 0
    pos2 = 0

    while pos1 < len1 and pos2 < len2:
        if list1[pos1] <= list2[pos2]:
            final_list.append(list1[pos1])
            pos1 += 1
        else:
            final_list.append(list2[pos2])
            pos2 += 1

    if pos1 < len1:
        final_list.extend(list1[pos1:])
    elif pos2 < len2:
        final_list.extend(list2[pos2:])

    return final_list

def task6():
    again = "Y"

    while again == "Y":
        list1 = input("Input 1st sorted list of numbers [x1 x2 ...]: ").strip()
        list2 = input("Input 2nd sorted list of numbers [y1 y2 ...]: ").strip()

        list1 = str_list_to_num_list(list1.split(" "))
        list2 = str_list_to_num_list(list2.split(" "))

        merged = merge_lists(list1, list2)
        print(f"Merged list: \n{merged}")

        again = input("Try again [Y/N]? ").strip().upper()


'''
    Main
'''
def main():
    print("\n---- Task 1: Check if list is sorted ----"); task1()
    print("\n---- Task 2: Merge dictionaries ----"); task2()
    print("\n---- Task 3: Invert dictionaries ----"); task3()
    print("\n---- Task 4: List to dictionary ----"); task4()
    print("\n---- Task 5: String list to num list ----"); task5()
    print("\n---- Task 6: Merge list with assert ----"); task6()

if __name__ == "__main__":
    main()