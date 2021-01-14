
########################################################################
# #100DaysofCode                                      By Jonathan Rhau #
#                                                                      #
#                       Day 9 - Blind Auction                          #
#                                                                      #
########################################################################

from art import logo
import os

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def reset_screen():
  os.system("clear") if os.name == "posix" else os.system("cls")
  print(logo + "\n")

reset_screen()
play_msg = "Do you want to participate in a blind auction? Y or N: "

while(input(play_msg).lower() == "y"):
  blind_bids = []
  other_bidders = True

  while(other_bidders):
    reset_screen()
    name = input("What is you name?: ")
    bid = float(input("What is you bid?: $"))
    blind_bids.append({"name":name, "bid":bid})
    other_bidders = input("\nAre there other bidders? Y or N: ").lower() == "y"

  highest_player = {"name":"", "bid":0}
  for player in blind_bids:
    if player["bid"] > highest_player["bid"]:
      highest_player = player

  reset_screen()
  print(f"{highest_player['name']} has won the auction with a bid of ${highest_player['bid']:0.2f}\n")

  play_msg = "Do you want to do another round of blind auction? Y or N: "

print("\See you next time!")