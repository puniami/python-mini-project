import random


def dice(func):
    def inner():
        print("===========")
        func()
        print("===========")
    return inner

@dice
def one():
    print("|         |\n|    O    |\n|         |")

@dice
def two():
    print("|         |\n| O     O |\n|         |")

@dice
def three():
    print("|    O    |\n|    O    |\n|    O    |")

@dice
def four():
    print("| O     O |\n|         |\n| O     O |")

@dice
def five():
    print("| O     O |\n|    O    |\n| O     O |")

@dice
def six():
    print("| O     O |\n| O     O |\n| O     O |")

dice_mapping = {
                    1: one, 2: two, 3: three,
                    4: four, 5: five, 6: six
                }

def play():
    print("This is a dice stimulator")
    x = 'y'
    while x == 'y':
        number = random.randint(1, 6)
        dice_mapping[number]()
        x =  input("Press y to dice again ")
    
play()
