## Week 15 Learn Together

# Documentation for My OOP Classes

I have started to turn my dev2 into OOP but I got to figure out the turtle implementation
first so alot of these classes will be tentative.

### MenuOption Class
(May end up having multiple superclasses of this base class since I think I will need more functionality)
attributes
- name
-- (str) name of menu option
- content
-- the content of the class. Could be a number or multiple pieces of information.

methods
- load()
-- displays to the screen the content of class object

### Menu Class
attributes
- menuItems = []
-- list of MenuOption objects

methods
- refresh()
-- clears current display and displays the Menu


### Funky Dice Class
attributes
- dice = {}
-- an empty dictionary
- directions
-- The directions to follow
- sides
-- (int) the number of sides the dice will have
- name
-- the name of the dice object


methods
- set_number_of_sides()
-- user inputs the number of sides they want and sets the object's sides to the value of the user input
- set_faces()
-- user inputs anything and the sides of the dice are set to the value of the user input
- set_name()
-- user inputs what they want the dice to be called and the object's name is set to the input
- create()
-- creates a custom dice with the other methods and adds the current created dice into the empty dictionary
- reset()
-- empties the content inside dice and makes all the other attributes empty strings or 0
