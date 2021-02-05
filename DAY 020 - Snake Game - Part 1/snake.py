########################################################################
# #100DaysofCode                                      By Jonathan Rhau #
#                                                                      #
#                      Day 20 - Sanke Game (p1)                        #
#                                                                      #
########################################################################


from turtle import Turtle

INIT_POS_X = 0
INIT_POS_Y = 0
INIT_SNAKE_LENGHT = 3
SNAKE_SHAPE = "square"
SNAKE_COLOR = "white"
SNAKE_SIZE = 20

# Head pointing direction
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake():

    def __init__(self):
        self.snake = [
            self._segment_factory(
                x=INIT_POS_X - (i * SNAKE_SIZE),
                y=INIT_POS_Y
            )
            for i in range(INIT_SNAKE_LENGHT)
        ]

        self.head = self.snake[0]
        self.body = self.snake[1:]

    def _segment_factory(self, x, y):
        segment = Turtle(shape=SNAKE_SHAPE)
        segment.penup()
        segment.color(SNAKE_COLOR)
        segment.goto(x, y)
        return segment

    def move(self):
        next_pos = self.head.pos()

        # Move the head
        self.head.forward(SNAKE_SIZE)

        # Follow your front segment
        for body_segment in self.body:
            curr_pos = body_segment.pos()
            body_segment.goto(next_pos)
            next_pos = curr_pos

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



