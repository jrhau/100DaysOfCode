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
    
while not at_goal():
    # Everytime we move, check if we are at goal
    while front_is_clear() and not at_goal():
        move_right()

    turn_left() if right_corner() else turn_right()