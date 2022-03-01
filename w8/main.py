# # REQUIREMENTS
# gets user input, at least 2 inputs
# If, elif, else
# comparison operators
# random
# f strings
# list
# loops

# Allow the user to run code until they want to stop
# Once they stop do some type of reporting back to the user, based on input
# Use nested-dictionary or nested-list or similar to save the input data.
# Don't use your dev work
# Needs to use functions and return values

# # WEEK 8 LEARN TOGETHER
# A decision I have to make alot: What to eat?
# Week 4 updated
import random
from list_of_characters import chars_list
from os import system

restart = False
end_program = False
no_more_food = False

# a dictionary nested with empty list
food_options = {
    "fridge": [],
    "freezer": [],
    "other": []
}
final_options = []
final_meal = ""


# Functions


def typo():
    # Function that determines if user inoutted a typo
    # global variable just calls the global version
    global end_program
    typo = input('Was that a typo?\nType "y" for yes or "n" for no\n>> '
                 ).lower()
    if typo == "y":
        return "Alright.\n"
    elif typo == "n":
        end_program = True
        return "\nCome back when you are feeling hungry."
    else:
        end_program = True
        return ("\nI will assume you weren't sure. Have a nice day and"
                " restart if you're hungry.")


def specific_typo_for_more_food():
    global no_more_food
    typo = input('Was that a typo?\nType "y" for yes or "n" for no\n>> '
                 ).lower()
    if typo == "y":
        return "Alright.\n"
    elif typo == "n":
        no_more_food = True
        return "\nOkay. Continue On."
    else:
        no_more_food = True
        return ("\nI will assume you are done with adding food options.")


def add_to_dictionary():
    global food_options
    global final_options
    for key in food_options:
        if int(len(food_options[key])) > 0:
            final_options.append(random.choice(food_options[key]))


def add_to_food_locations(location):
    global food_options
    if location in food_options:
        user_food = input("\nWhat food or dish do you feel like eating from "
                          f"{location}?\n>> ")
        if user_food == "" or user_food == " ":
            return "That's no a valid option"
        else:
            food_options[location].append(user_food)
        return f"{user_food} has been noted as in the {location}.\n"
    else:
        return "That's not a valid option\n"


def final_selection():
    global end_program
    global no_more_food
    global food_options
    global final_options
    global final_meal
    # gives user option and asks them to choose from the options
    final_q = input(f"\nOut of the avaliable options, which do you feel"
                    f" like eating the most?\n\n{final_options}\n\n"
                    "Choose one.\n But if you want to choose multiple,"
                    ' Make sure to seperate them with a comma ","'
                    '\nYour Imput>> '
                    ).split(",")
    # determines meal depending on the amount of items the user inputted
    if len(final_q) == 1:
        for item in final_q:
            final_meal += item
        end_program = True
        return f"\nYour next meal is {final_meal}.\n"
    elif len(final_q) > 1:
        decide = random.randint(0, len(final_q) - 1)
        final_meal = final_q[decide]
        end_program = True
        return ("\nSince you couldn't decide, I decided for you. "
                f"Your next meal will be {final_meal}\n")
    else:
        end_program = True
        return "Are you skipping on this meal? That's no good."


print("\nWelcome to my meal decision helper.")
print("\nThis program is to help you decide"
      " what to eat based on food options you give it.\n\n")
print("Now the big question of the day!")


def meal_decision_helper():
    global end_program
    global no_more_food
    global food_options
    global final_options
    global final_meal
    user = input("Are you hungry?\n"
                 'Type "Y" for yes and "N" for no\nYour Input>> ').lower()

    while end_program is False:
        if user == "y":
            # Loop for user to add food items into list located in the
            # dictionary food_options
            while no_more_food is False:
                print(
                    add_to_food_locations(
                        input("\nWhere would you like to look first for food?"
                              "\nType one of the following options to start.\n"
                              "\nFridge\nFreezer\nOther\nYour Input>> "
                              ).lower()
                        )
                    )
                more_food = input("\nDo you want to keep adding more food you "
                                  'feel like eating?\nType "Y" for yes or "N" '
                                  "for no\nYour Input>> ").lower()
                if more_food == "n":
                    no_more_food = True
                elif not more_food == "y" and more_food in chars_list:
                    print(specific_typo_for_more_food())

        # continues the code direction towards the meal selection
            question = input("Do you think you know what you feel like eating?"
                             '\n "Y" or "N"\nYour Input>> ').lower()

            if question == "y":

                # this is to get a number to be used in a range later
                amount = int(input("\nGive me a number and I will give you "
                                   "some options.\nYour Input>> ")) + 1

        # figures out if user input is found in the chars_list and ends loop.
                if amount in chars_list:
                    print("You're skipping this meal? That's not good.")
                    end_program = True

        # adds random number of food items in nested list to final_option list
                for number in range(1, amount):
                    add_to_dictionary()
                print(final_selection())

        # determines the user's meal with only the initial lists they made
            elif question == "n":
                total_length_of_list = 0
                for key in food_options:
                    total_length_of_list += int(len(food_options[key]))

            # Random_op stands for random option
            # Through random, program determines user's meal
                random_op = random.randint(0, total_length_of_list)
                for food in range(1, random_op + 1):
                    add_to_dictionary()
                final_option = random.choice(final_options)
                print("\nI've decided that your next meal will be "
                      f"{final_option}.\n")
                end_program = True

        # if user had invalid input
            else:
                print(typo())

        # other direction that ends the code
        elif user == "n":
            print("Come back when you are feeling hungry.")
            end_program = True

        # just for fun but does basically the same thing as the one right above
        else:
            print(typo())


# loop that keeps the program running as long as user wants it to be
while restart is False:
    meal_decision_helper()
    user_option = input("Do you want to continue using this program"
                        ' without restarting it?\nType "Y" for yes and '
                        "anything else for no\nUser Input>> ").lower()
    if user_option == "y":
        system("cls")
    else:
        print("\nThank you. Come Back Soon.")
        restart = True
