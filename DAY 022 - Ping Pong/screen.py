########################################################################
# #100DaysofCode                                      By Jonathan Rhau #
#                                                                      #
#                      Day 22 - Ping Pong Game                         #
#                                                                      #
########################################################################


from turtle import Screen, Turtle
from time import sleep


class Board():
    SCREEN_BG = "black"
    SCREEN_SIZE = (1000,600)
    SCREEN_REFRESH_RATE = 0.05
    SCREEN_TITLE = "DAY 022 - Ping Pong Game"
    MIDDLE_LINE_COLOR = "white"
    MIDDLE_LINE_SIZE = 10

    def __init__(self):
        self.screen = Screen()
        self.screen.bgcolor(self.SCREEN_BG)
        self.screen.setup(*self.SCREEN_SIZE)
        self.screen.title(self.SCREEN_TITLE)
        self.speed = self.SCREEN_REFRESH_RATE
        self.screen.tracer(0)

        self._draw_mid_line()
        self.refresh()

    def _draw_mid_line(self):
        t = Turtle(visible=False)
        t.penup()
        t.goto(0, self.SCREEN_SIZE[1]/-2)
        t.setheading(90)
        t.color(self.MIDDLE_LINE_COLOR)
        t.pensize(self.MIDDLE_LINE_SIZE)

        while t.pos()[1] <= self.SCREEN_SIZE[1]/2:
            t.penup() if t.pos()[1] % 40 else t.pendown()
            t.forward(20)

    def refresh(self):
        self.screen.update()
        sleep(self.speed)

    def accelerate(self):
        self.speed *= 0.8

    def reset(self):
        self.speed = self.SCREEN_REFRESH_RATE
        t = Turtle(visible=False)
        t.color("red")
        t.goto(0,-60)
        for count in range(3,0,-1):
            t.write(str(count), align="center", font=("Arial", 120, "bold"))
            sleep(1)
            t.clear()