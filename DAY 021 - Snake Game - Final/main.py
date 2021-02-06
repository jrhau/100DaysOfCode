########################################################################
# #100DaysofCode                                      By Jonathan Rhau #
#                                                                      #
#                    Day 20 - Sanke Game (final)                       #
#                                                                      #
########################################################################

from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

SCREEN_BG = "black"
SCREEN_SIZE = (600,600)
SCREEN_REFRESH_RATE = 0.1
SCREEN_TITLE = "DAY 020 - Snake Game -part 1"

screen = Screen()

screen.bgcolor(SCREEN_BG)
screen.setup(*SCREEN_SIZE)
screen.title(SCREEN_TITLE)
screen.tracer(0)


snake = Snake(SCREEN_SIZE)
food = Food(SCREEN_SIZE)
score = Score(SCREEN_SIZE)

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
    
    screen_refresh()
    game_on = snake.move()

    if snake.head.distance(food) <= 18:
        food.refresh()
        snake.growth()
        score.increase()

score.game_over()

screen.exitonclick()
