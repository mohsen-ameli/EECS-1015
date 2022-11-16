##################################
# EECS1015 - York University
# Author: Michael S. Brown 
# (c) MS Brown. This code cannot be shared without permission from the
# author.
# Lab 8 starter code
#
##################################
import random


'''
    Task 0
'''
def print_student_info():
    print("---- Lab 8 ----")
    print("Name: Mohsen Ameli")
    print("Section A")
    print("Student id: 219705755")
    print("Email: noobmoe@my.yorku.ca")

def task0():
    print_student_info()


'''
    Task 1
'''
def lotto_draw():
    set_num = 0
    num = set()

    while set_num != 5:
        rand = random.randrange(1, 20)

        if rand not in num:
            num.add(rand)
            set_num += 1
    
    return num

class lotto_ticket():
    ticket_counter = 1

    def __init__(self):
        self.ticket_id = lotto_ticket.ticket_counter
        lotto_ticket.ticket_counter += 1

        self.number = lotto_draw()
    
    def print_ticket(self):
        print(f"Ticket #[{self.ticket_id:3d}]", end="")

        for num in self.number:
            print(f"  {num:2d}  ", end="")
        
        print()
    
    def print_and_return_win(self, lotto_numbers):
        num_matches = 0

        # printing ticket id
        print(f"Ticket #[{self.ticket_id:3d}]", end="")

        for item in lotto_numbers:
            if item in self.number:
                num_matches += 1
                print(f" *{item:02d}* ", end="")
            else:
                print(f"  {item:02d}  ", end="")

        if num_matches == 3:
            win_amount = 2
        elif num_matches == 4:
            win_amount = 20
        elif num_matches == 5:
            win_amount = 100
        else:
            win_amount = 0
        
        print(f"\t[{num_matches} matche(s), ${win_amount}]")

        return win_amount

def task1():
    exit_ = False
    ticket_price = 2
    amount = 100

    while not exit_ and amount >= ticket_price:
        get_num_tickets = True

        while get_num_tickets:
            print(f"You have ${amount}.")

            num_tickets = int(input(f"How many lotto tickets do you want [${ticket_price} each]? "))

            if num_tickets * ticket_price > amount or num_tickets < 0:
                get_num_tickets = True
            elif get_num_tickets == 0:
                exit_ = True
                get_num_tickets = False
            else:
                amount -= (num_tickets * ticket_price)
                get_num_tickets = False
        
        tickets = []

        for i in range(num_tickets):
            tickets.append(lotto_ticket())
            tickets[i].print_ticket()
        
        print("--LOTTO DRAW--")
        lotto = lotto_draw()
        for i in lotto:
            print(i, end=" ")
        print()

        print("---Press enter to check your winnings---", end="")
        input()

        # printing winning tickets
        for ticket in tickets:
            win_amount = ticket.print_and_return_win(lotto)
            amount += win_amount
 
    print("You lost! [money: $0]")


'''
    Task 2
'''
class virus:
    pass

def task2():
    pass


'''
    Main
'''
def main():
    task0()
    print("\n--- Task 1: Lotto LESS Revisited ---")
    task1()
    print("\n--- Task 2: Virus mutator ---")
    task2()

if __name__ == "__main__":
      main()