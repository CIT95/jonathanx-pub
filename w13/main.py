from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("grey")

user_bet = screen.textinput(title="make your bet",
                            prompt="Which turtle will win the race"
                                   "? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-75, -45, -15, 15, 45, 75]
all_turtles = []

writer = Turtle()
writer.hideturtle()
writer.penup()

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    # added lap to Turtle
    # to be kind of like racing games where it takes multiple laps to win
    new_turtle.lap = 0
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    new_turtle.speed(0)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on is True:

    for turtle in all_turtles:
        # victory is based on if the turtle passed the line and if they are in
        # the last lap of the race
        if turtle.xcor() > 230 and turtle.lap == 2:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                # writes the winning message to the window instead of terminal
                screen.clear()
                screen.bgcolor(turtle.pencolor())
                writer.write(
                    f"You've won! The {winning_color} turtle is the winner.",
                    move=True, align="center",
                    font=("Arial", 16, "bold"))
            else:
                # same as above except for the losing message
                screen.clear()
                screen.bgcolor(turtle.pencolor())
                writer.write(
                    f"You've lost! The {winning_color} turtle is the winner.",
                    move=True, align="center",
                    font=("Arial", 16, "bold"))
        elif turtle.xcor() > 250:
            # makes it so the turtles look like they traveled around
            # back to the start
            turtle.hideturtle()
            turtle.setx(-270)
            turtle.showturtle()
            turtle.lap += 1
        else:
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)

screen.exitonclick()
