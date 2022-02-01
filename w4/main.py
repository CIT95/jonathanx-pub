# Week 4 Learn Together

import random

# A decision I have to make alot: What to eat?

# I ported over the list of letters from the day 5 final and added empty spaces
# into the list for usage in a portion of my code later
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
            'Y', 'Z', "", " "]
# an empty list for items to be added into later
options = []

# empty string to be used later
final_meal = ""

print("\nWelcome to my meal decision helper.")
# first input that determines the direction of the code
user = input("The big question of the day. Are you hungry?\n"
             'Type "Y" for yes and "N" for no\n>> ').lower()

if user == "y":
    print("\nThen you've come to the right person. Head to the kitchen.")

# each creates a list from user input that splits words based on a comma
    fridge = input("\nWhat's in your fridge?\nType foods in your fridge"
                   ' with a comma "," between each food.\n>>').split(",")
    freezer = input("\nHow about your freezer?\nType foods in your fridge"
                    ' with a comma "," between each food.\n>>').split(",")
    other = input("\nIs there any other food you feel like eating?"
                  '\nType the remaining food with a comma "," between each'
                  "\n>> ").split(",")

# continues the code direction towards the meal selection
    question = input("Do you think you know what you feel like eating?"
                     '\n "Y" or "N"\n>> ').lower()

    if question == "y":
        print("\nGive me a number and I will give you options.")

# like the day 5 final, this is to get a number to be used in a range later
        fridge_options = input("\nHow many food do you feel like eating from"
                               " the fridge?\n>> ")
        freezer_options = input("\nHow many food do you feel like eating from"
                                " the freezer?\n>> ")
        other_options = input("\nHow many food do you feel like eating from"
                              " anywhere else?\n>> ")

# the snippet of code that uses the big list of characters at the beginning
# figures out if user input is found in the alphabet list
# if so, the input becomes equal to zero
        if fridge_options in alphabet:
            fridge_options = 0
        if freezer_options in alphabet:
            freezer_options = 0
        if other_options in alphabet:
            other_options = 0

# Like the Day 5 final, used to add random items from the three previous list
# into the empty list in the beginning of my code
        for food in range(1, int(fridge_options) + 1):
            options.append(random.choice(fridge))
        for food in range(1, int(freezer_options) + 1):
            options.append(random.choice(freezer))
        for food in range(1, int(other_options) + 1):
            options.append(random.choice(other))

# Just to prevent any bugs when user inputs nothing
        if len(options) == 0:
            print("You're skipping this meal? That's not good.")

        else:
            # gives user option and asks them to choose from the options
            final_q = input(f"\nout of the options, which do you feel like"
                            f" eating the most?\n\n{options}\n\n"
                            "Choose up to two. Make sure to seperate them "
                            'with a comma ","\n>> ').split(",")
# each determine your meal depending on the amount of items the user inputted
            if len(final_q) == 1:
                for item in final_q:
                    final_meal += item
                print(f"Your next meal is {final_meal}.")
            elif len(final_q) > 1:
                coin = random.randint(0, len(final_q) - 1)
                final_meal = final_q[coin]
                print("Since you couldn't decide,"
                      " I decided for you."
                      f"Your next meal will be {final_meal}")
            else:
                print("Are you skipping on this meal? That's no good.")

# determines the user's meal with only the initial lists they inputted
# the length of each list to be used to determine user's meal
    elif question == "n":
        fridge_length = len(fridge) - 1
        freezer_length = len(freezer) - 1
        other_length = len(other) - 1

# Random_op stands for random option
        random_op1 = random.randint(0, freezer_length)
        random_op2 = random.randint(0, freezer_length)
        random_op3 = random.randint(0, other_length)

# same as earlier but with no user input
        for food in range(1, random_op1 + 1):
            options.append(random.choice(fridge))
        for food in range(1, random_op2 + 1):
            options.append(random.choice(freezer))
        for food in range(1, random_op3 + 1):
            options.append(random.choice(other))

        final_number = random.randint(0, len(options) - 1)
        final_option = options[final_number]
        print(f"I've decided that your next meal will be {final_option}.")

# if user never inputted anything from the start, this will print
    else:
        print("There was an error in my ability. Restart and try again.")

# other direction that ends the code
elif user == "n":
    print("Come back when you are feeling hungry.")

# just for fun but does basically the same thing as the one right above
else:
    typo = input("Was that a typo?\n"
                 '"Y" or "N"\n>> ').lower()

    if typo == "y":
        print("\nWell time to restart.")
    elif typo == "n":
        print("\nCome back when you are feeling hungry.")
    else:
        print("\nI will assume you weren't sure. Have a nice day and"
              " restart if you're hungry.")
