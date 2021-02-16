########################################################################
# #100DaysofCode                                      By Jonathan Rhau #
#                                                                      #
#                      Day 22 - Ping Pong Game                         #
#                                                                      #
########################################################################

from turtle import Turtle



class Score(Turtle):

    FONT = ("Arial", 64, "bold")
    ALIGNMENT = "center"
    TOP_PADDING = 100
    SCORE_COLOR = "white"

    def __init__(self, screensize):
        super().__init__(visible=False)

        self.screensize = screensize
        self.color(self.SCORE_COLOR)
        self.player_left = 0
        self.player_right = 0

        self._print_score()

    def _print_score(self):
        self.clear()
        for score, x_pos in [(self.player_left, -100), (self.player_right, 100)]:
            self.penup()
            self.goto(x_pos, self.screensize[1]/2 - self.TOP_PADDING)
            self.pendown()
            self.write(str(score), align=self.ALIGNMENT, font=self.FONT)

    def increase(self, exit_left, exit_right):

        if exit_right: self.player_left += 1
        if exit_left: self.player_right += 1
        
        self._print_score()

