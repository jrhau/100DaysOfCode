########################################################################
# #100DaysofCode                                      By Jonathan Rhau #
#                                                                      #
#                      Day 18 - Hirst Painting                         #
#                                                                      #
########################################################################
import colorgram
import random
import turtle

colors = colorgram.extract('image.jpg', 30)
rgb_colors = [color.rgb for color in colors]

turtle.colormode(255)
cursor = turtle.Turtle()
cursor.penup()

for row in range(1,11):
    cursor.setpos(-225, 50*row-275)
    for _ in range(10):
        cursor.dot(20, random.choice(rgb_colors))        
        cursor.forward(50)

screen = turtle.Screen()
screen.exitonclick()