########################################################################
# #100DaysofCode                                      By Jonathan Rhau #
#                                                                      #
#                     Day 4 - Rock Paper Scissors                      #
#                                                                      #
########################################################################

from utils import rock, paper, scissors, print_result
import random

choices = [rock, paper, scissors]

print("Welcome to the Rock, Paper, Scissors challenge!")

play_msg = "Wanna Play? Y or N: "

while(input(play_msg).lower() == "y"):
  p1 = input("What do you choose?\n\t0 = Rock\n\t1 = Paper \n\t2 = Scissors\n\nYou choose: ")

  # Restart the whileloop if invalid choice 
  if p1 != "0" and p1 != "1" and p1 != "2":
    print("Invalid choice...")
    continue

  p1 = int(p1)
  pc = random.choice(choices)

  print_result(choices[p1], pc)

  # Using a circular logic where I compare if my choice is located
  # before or after the computer choice in my choices list.
  if choices[p1] == pc:
    print("This is a DRAW!")
  elif choices[p1 -1] == pc:
    print("You WON!")
  else:
    print("You LOST!")


  play_msg = "\nWanna play again? Y or N: "