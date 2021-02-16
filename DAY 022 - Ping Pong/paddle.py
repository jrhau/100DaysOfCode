########################################################################
# #100DaysofCode                                      By Jonathan Rhau #
#                                                                      #
#                      Day 22 - Ping Pong Game                         #
#                                                                      #
########################################################################

from turtle import Turtle

class Paddle(Turtle):
    PADDLE_LENGHT = 8
    PADDLE_SHAPE = "square"
    PADDLE_COLOR = "white"
    STEP_SIZE = 50

    def __init__(self, location):
        super().__init__(shape=self.PADDLE_SHAPE)
        self.penup()
        self.color(self.PADDLE_COLOR)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(location, 0)

    def up(self):
        x, y = self.pos()
        self.goto(x, y + self.STEP_SIZE)

    def down(self):
        x, y = self.pos()
        self.goto(x, y - self.STEP_SIZE)

    def reset(self):
        self.sety(0)
