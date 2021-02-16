########################################################################
# #100DaysofCode                                      By Jonathan Rhau #
#                                                                      #
#                      Day 22 - Ping Pong Game                         #
#                                                                      #
########################################################################

from screen import Board
from score import Score
from paddle import Paddle
from ball import Ball

board = Board()
score = Score(board.SCREEN_SIZE)
ball = Ball(board.SCREEN_SIZE)


p_left = Paddle(board.SCREEN_SIZE[0]/-2 + 20)
p_right = Paddle(board.SCREEN_SIZE[0]/2 - 25)

board.refresh()

board.screen.listen()
board.screen.onkeypress(p_left.up, "w")
board.screen.onkeypress(p_left.down, "s")
board.screen.onkeypress(p_right.up, "Up")
board.screen.onkeypress(p_right.down, "Down")

while True:

    board.refresh()

    # Using the heading direction to fix some instance where the ball would
    # rebounce multiple time on the same paddle.
    heading_left = 90 < ball.heading() < 270

    # Make the ball bounce only if it is headding the proper direction
    for paddle, proper_direction in [(p_left, heading_left), (p_right, not heading_left)]:
        if all([ball.distance(paddle) <= 50, abs(paddle.xcor() - ball.xcor()) <= 25, proper_direction]):
            ball.bounce(ball.distance(paddle))
            board.accelerate()

    exit_direction = ball.move()

    if any(exit_direction):
        score.increase(*exit_direction)
        for func in [ball, p_left, p_right, board]:
            func.reset()


board.screen.exitonclick()
