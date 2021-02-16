########################################################################
# #100DaysofCode                                      By Jonathan Rhau #
#                                                                      #
#                      Day 22 - Ping Pong Game                         #
#                                                                      #
########################################################################

from turtle import Turtle
from random import randint, random, choice

class Ball(Turtle):
    SHAPE = "circle"
    COLOR = "blue"

    def __init__(self, screensize):
        super().__init__(shape=self.SHAPE)

        # [x_min, x_max, y_min, y_max]
        self.edge = [edge/2 * factor for edge in screensize for factor in (-1, 1)]

        self.penup()
        self.color(self.COLOR)

        self.direction = 0
        self.reset()

    def move(self):
        self.forward(10)

        # If distance to top or bottom edge is less or equal to 10 pixel
        if any([abs(self.ycor() - edge) <= 10 for edge in self.edge[2:]]):
            # Bounce by the impact angle
            self.setheading(360 - self.heading())

        x_min, x_max = self.edge[:2]

        # Return (has_exit_left, has_exit_right)
        return self.xcor() <= x_min, self.xcor() >= x_max


    def bounce(self, distance):
        # If the ball is closer to the edge (higher distance), the variance has 
        # a greater range. If the ball is right in the middle (distance = 20),
        # the variance will be 0
        variance = random() * (distance-25) * choice((1, -1))
        self.setheading(180 - self.heading() + variance)

    def reset(self):
        self.goto(0,0)
        self.direction = 0 if self.direction else 180
        self.setheading(randint(140,200) + self.direction)
        
        
