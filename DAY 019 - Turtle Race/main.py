########################################################################
# #100DaysofCode                                      By Jonathan Rhau #
#                                                                      #
#                        Day 19 - Turtle Race                          #
#                                                                      #
########################################################################

from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

def turtle_generator(color, x, y):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x=x, y=y)
    
    return new_turtle

#Create 6 turtles
all_turtles = [turtle_generator(color=color, x=-230, y=y) for color, y in zip(colors, y_positions)]

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        #230 is 250 - half the width of the turtle.
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            result = "won" if winning_color == user_bet else "lost"
            print(f"You've {result}! The {winning_color} turtle is the winner!")

        #Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()