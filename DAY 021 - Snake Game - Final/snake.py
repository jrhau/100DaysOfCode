########################################################################
# #100DaysofCode                                      By Jonathan Rhau #
#                                                                      #
#                    Day 20 - Sanke Game (final)                       #
#                                                                      #
########################################################################

from turtle import Turtle

INIT_POS_X = 0
INIT_POS_Y = 0
INIT_SNAKE_LENGHT = 3
TAIL_LENGHT = 3
BODY_SIZE = 20
BODY_SHAPE = "square"
BODY_COLOR = "white"
HEAD_SHAPE = "circle"
HEAD_COLOR = "yellow"
TAIL_SHAPE = "circle"
FED_COLOR = "green"


# Head pointing direction
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake():

    def __init__(self, screensize=(300, 400)):

        # Screen axis range (min,max) while considering the snake
        self.x_range, self.y_range = [
            tuple((size//2 + BODY_SIZE//2) * factor for factor in [-1, 1])
            for size in screensize
        ]

        # Creating the whole snake
        self.snake = [
            self._segment_factory(INIT_POS_X - (i * BODY_SIZE), INIT_POS_Y)
            for i in range(INIT_SNAKE_LENGHT + TAIL_LENGHT)
        ]

        # Defining the snake head
        self.head = self.snake[0]
        self.head.shape(HEAD_SHAPE)
        self.head.color(HEAD_COLOR)

        # Defining the snake body
        self.body = self.snake[1:-TAIL_LENGHT]

        self.set_tail()

    def set_tail(self):
        self.tail = self.snake[-TAIL_LENGHT:]

        factor = 1 - 1/(TAIL_LENGHT + 1)
        for segment in self.tail:
            segment.shape(TAIL_SHAPE)
            segment.shapesize(factor, factor)

            factor -= 1/(TAIL_LENGHT + 1)

    def _segment_factory(self, x, y):
        segment = Turtle(shape=BODY_SHAPE)
        segment.penup()
        segment.color(BODY_COLOR)
        segment.goto(x, y)
        return segment

    def growth(self):
        # Inserting a the end of the snake body a new segment
        self.snake.insert(-TAIL_LENGHT, self._segment_factory(*self.snake[-TAIL_LENGHT].pos()))
        self.body = self.snake[1:-TAIL_LENGHT]
        self.tail = self.snake[-TAIL_LENGHT:]
        self.body[0].color(FED_COLOR)

    def move(self):
        front_pos = self.head.pos()
        front_col = BODY_COLOR

        # Move the head
        self.head.forward(BODY_SIZE)

        # Follow your front segment and front color
        for segment in self.snake[1:]:
            curr_pos = segment.pos()
            curr_col = segment.color()[0]

            segment.goto(front_pos)
            segment.color(front_col)

            front_pos = curr_pos
            front_col = curr_col

        # Detect Wall Colision
        if not self.x_range[0] < self.head.xcor() < self.x_range[1] or \
           not self.y_range[0] < self.head.ycor() < self.y_range[1]:
            return False

        # Detect Self Colision.
        # Touching the tail is ok tho... We are nice
        for segment in self.body:
            if self.head.distance(segment) < BODY_SIZE // 2:
                return False

        return True

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
