########################################################################
# #100DaysofCode                                      By Jonathan Rhau #
#                                                                      #
#                       Day 14 - High or Low                           #
#                                                                      #
########################################################################
from art import logo, vs
import game_data
import random
import os
import copy


def reset_screen() -> None:
    """Clears the screen and print the game logo"""
    os.system("clear") if os.name == "posix" else os.system("cls")
    print(logo)
    print("=" * 80)

play_msg = "Wanna play? Y or N: "

reset_screen()
while(input(play_msg).lower() == "y"):
  play_msg = "Wanna play again? Y or N: "

  # using deepcopy to get a new list at a new memory address location
  data = copy.deepcopy(game_data.data)
  random.shuffle(data)

  fight = [data.pop()]
  score = 0

  # Round start
  while(True):
    
    # If you are too good...
    if len(data) > 0:
      fight.append(data.pop())
    else:
      print("You have found them all!")
      print("I here by grant you the title of Grand Master!\n")
      break

    # Debug
    # print([x["follower_count"] for x in fight])

    print(f"Compare A: {fight[0]['name']}, a {fight[0]['description']}, from {fight[0]['country']}.")
    print(vs)
    print(f"\nAgainst B: {fight[1]['name']}, a {fight[1]['description']}, from {fight[1]['country']}.")

    # Input validation loop
    while(True):
      answer = input("\nWho has the more folloers? A or B: ").lower()

      if answer == "a" or answer == "b":
        break
      else:
        print(f"'{answer}' is not valid. You must choose 'A' or 'B'")
        input("I understand...")


    if (answer == "a" and fight[0]["follower_count"] >= fight[1]["follower_count"]) or (answer == "b" and fight[1]["follower_count"] >= fight[0]["follower_count"]):
      score += 1
      print(f"\nYour are right! You have {score} points.")
      input("Continue...")

      # Remove fighter A and add a new fighter at the end of list
      fight.pop(0)
    else: 
      print("\nYou are wrong...")
      input(f"You have finished with {score} points.\n")
      break

    reset_screen()

print("See you next time!")