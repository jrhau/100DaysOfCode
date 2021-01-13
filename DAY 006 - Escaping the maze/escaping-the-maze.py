########################################################################
# #100DaysofCode                                      By Jonathan Rhau #
#                                                                      #
#                     Day 6 - Escaping the maze                        #
#                                                                      #
########################################################################

# This code is meant to be run on Reeborg's World to solve the maze challenge
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def right_corner():
    return wall_in_front() and wall_on_right()

def move_right():
    move()
    if right_is_clear():
        turn_right()
        
# Let's found our first wall and lean on it
while front_is_clear() and not at_goal():
    move()
while right_is_clear():
    turn_right()
    
# Move forward while seeking the right
while not at_goal():
    while front_is_clear() and not at_goal():
        move_right()
    turn_left() if right_corner() else turn_right()