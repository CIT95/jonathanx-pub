# Day 1 ex3 code for Learn Together W2

# # Original Code
# name = input("What is your name? ")
# print(len(name))

# # Modified Code
name = input("What's your name?\n")

# Gets the length of the user's name
name_length = len(name)

# Finds the position of the last letter in the user's name
name_position = int(name_length) - 1


first_letter = name[0]
last_letter = name[name_position]

# Prints user's name length, first letter, and last letter of their name.
print(f'Your name has {name_length} letters.\n'
      + f'The first letter in your name is "{first_letter}"\n'
      + f'The last letter in your name is "{last_letter}"')
