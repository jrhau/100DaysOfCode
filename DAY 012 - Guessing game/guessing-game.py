
########################################################################
# #100DaysofCode                                      By Jonathan Rhau #
#                                                                      #
#                        Day 12 - Guessing game                        #
#                                                                      #
########################################################################
import os, random

logo = """\
 _______                         __                  _______                      
|     __.--.--.-----.-----.-----|__.-----.-----.    |     __.---.-.--------.-----.
|    |  |  |  |  -__|__ --|__ --|  |     |  _  |    |    |  |  _  |        |  -__|
|_______|_____|_____|_____|_____|__|__|__|___  |    |_______|___._|__|__|__|_____|
                                         |_____|                                  

"""
def reset_screen() -> None:
    """Clears the screen and print the game logo"""
    os.system("clear") if os.name == "posix" else os.system("cls")
    print(logo)
    print("=" * 80)

play_msg = "Wanna play the guessing game? Y or N: "


reset_screen()
while(input(play_msg).lower() == "y"):
  play_msg = "Wanna play the guessing game again? Y or N: "
  reset_screen()
  while(True):
    difficulty = input("Choose a difficulty level: easy or hard: ").lower()

    if difficulty == "easy" or difficulty == "hard":
      break
    else:
      input(f"'{difficulty}' is not a valid option.\nI understand...")
      reset_screen()

  guess_setting = {"easy": 10, "hard": 5}

  attempts = guess_setting[difficulty]

  magic_number = random.randint(1,101)

  reset_screen()
  print("I chosed a number between 1 and 100.")
  print(f"Can you guess that number in {attempts} or less attempts?\n")

  while(attempts>0):
    while(True):
      try:
        guess = int(input("Make a guess: "))

        if 1 <= guess <= 100:
          break
        else:
          input(f"'{guess}' is not valid. You must choose between 1 and 100.\nI understand...")
      except:
        input("You must choose a number between 1 and 100.\nI understand...")

    if guess == magic_number:
      print(f"\nYou are right!!!")
      break
    
    attempts -= 1
    
    if attempts == 0:
      print("\nYou have no more attempts left. Sorry...")
    else:
      print("Too low..." if guess < magic_number else "Too high...")
      print(f"You have {attempts} attempts left.")

  input(f"'{magic_number}' was the magic number!")
  reset_screen()
