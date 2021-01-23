########################################################################
# #100DaysofCode                                      By Jonathan Rhau #
#                                                                      #
#                         Day 17 - Quiz Game                           #
#                                                                      #
########################################################################

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = [Question(**QA) for QA in question_data]
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was {quiz.score}/{quiz.question_number}")