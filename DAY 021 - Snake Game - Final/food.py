########################################################################
# #100DaysofCode                                      By Jonathan Rhau #
#                                                                      #
#                    Day 21 - Sanke Game (final)                       #
#                                                                      #
########################################################################

from turtle import Turtle
from random import randint

FOOD_SHAPE = "circle"
FOOD_COLOR = "green"
FOOD_SIZE_RATIO = 0.5
SPEED = "fastest"
MARGIN = 40


class Food(Turtle):

    def __init__(self, screensize=(300,400)):
        super().__init__(shape=FOOD_SHAPE)

        # Screen axis range (min,max) while considering a border margin
        self.x_range, self.y_range = [
            tuple((size // 2 - MARGIN)*factor for factor in [-1, 1]) 
            for size in screensize
        ]

        self.penup()
        self.color(FOOD_COLOR)
        self.shapesize(*[FOOD_SIZE_RATIO]*2)
        self.speed(SPEED)

        self.refresh()

    def refresh(self):
        self.goto(x=randint(*self.x_range), y=randint(*self.y_range))
