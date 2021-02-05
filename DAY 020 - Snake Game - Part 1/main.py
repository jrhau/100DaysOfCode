########################################################################
# #100DaysofCode                                      By Jonathan Rhau #
#                                                                      #
#                      Day 20 - Sanke Game (p1)                        #
#                                                                      #
########################################################################

from turtle import Screen
from snake import Snake
import time

SCREEN_BG = "black"
SCREEN_SIZE = {"width": 600, "height": 600}
SCREEN_REFRESH_RATE = 0.1
SCREEN_TITLE = "DAY 020 - Snake Game - Part 1"

screen = Screen()
screen.bgcolor(SCREEN_BG)
screen.setup(**SCREEN_SIZE)
screen.title(SCREEN_TITLE)
screen.tracer(0)


snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

def screen_refresh():
    screen.update()
    time.sleep(SCREEN_REFRESH_RATE)


game_on = True
while game_on:
    snake.move()
    screen_refresh()

screen.exitonclick()
