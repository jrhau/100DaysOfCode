########################################################################
# #100DaysofCode                                      By Jonathan Rhau #
#                                                                      #
#                    Day 20 - Sanke Game (final)                       #
#                                                                      #
########################################################################

from turtle import Turtle

SCORE_COLOR = "white"
FONT = ("Arial", 16, "bold")
ALIGNMENT = "center"
TOP_PADDING = 30

class Score(Turtle):
    
    def __init__(self, screensize=(300,400)):
        super().__init__(visible=False)

        self.score = 0
        self.goto(0, screensize[1]//2-TOP_PADDING)
        self.color(SCORE_COLOR)
        self._print_score()
        

    def increase(self):
        self.score += 1
        self.clear()
        self._print_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def _print_score(self):
        self.write(f"SCORE: {self.score}", align=ALIGNMENT, font=FONT)