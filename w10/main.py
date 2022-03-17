# # Week 10 Learn Together

# Funky Dice Program

# Imports
import random
from os import system

# Variables
result == ""
funky_dice = {}
end_program = False

# Functions


def set_dice_face(side):
    global funky_dice
    face = input("What do you want this side of the dice to be?\n>> ")
    funky_dice[side] = face
    return f"\nThe value of Side {side} is set to '{face}'."


def roll():
    global result
    result = funky_dice[random.randint(1, 6)]
    return result


def get_result():
    roll_result = roll()
    return f"\nYou roll the funky dice and get {roll_result}."


# Program

print("\nWelcome to Funky Dice!")
print("We give you a blank dice and you decide what the sides will be.")
print(The sides can be anything from numbers, names, or even nothing.)
print("It's entirely up to you.\n")

while not end_program
    for value in range(6):
        print(set_dice_face(value + 1))

    roll_option = input("\nDo you want to roll your dice?\n"
                        "Type 'Y' for yes and 'N' for no.\n"
                        ">> ").lower()

    if roll_option == "y":
        end_roll = False
        print(get_result())

        while not end_roll:
            again = input("\nDo you want to roll again?\n"
                          "Type 'Y' for yes and 'N' for no.\n"
                          ">> ").lower()
            if again == 'n':
                print(get_result())
            elif again == 'y':
                end_roll = True

        new_dice = input("\nDo you want to make a new dice?\n"
                         "Type 'Y' for yes and 'N' for no.\n"
                         ">> ").lower()

        # To either end or repeat the program
        if new_dice = 'y':
            system('cls')
            print("\nYou already know the rules.\n")
        else:
            end_program = True

    else:
    end_program = True

print("\nSee you next time.")
