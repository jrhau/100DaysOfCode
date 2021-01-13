########################################################################
# #100DaysofCode                                      By Jonathan Rhau #
#                                                                      #
#                           Day 7 - Hangman                            #
#                                                                      #
########################################################################
import random, os
from hangman_words import word_list
from hangman_art import stages, logo

def print_stage():
  print(stages[lives])
  print(' '.join(display))

def reset_screen():
  os.system("clear") if os.name == "posix" else os.system("cls")
  print(logo)

def error_msg(msg):
  print("\n" + msg)
  print("You are not penalize, but try again.")

play_msg = "\nWanna play? Y or N: "

reset_screen()

while(input(play_msg).lower() == "y"):
  reset_screen()

  chosen_word = random.choice(word_list)
  display = ["_" for _ in chosen_word]
  guess_history = []
  lives = 6

  print(f"\n\nYou have {lives} lives to guess the mistery word.")

  while display != list(chosen_word) and lives > 0:
    
    print_stage()

    guess = input("\n\nGuess a letter: ").lower()
    reset_screen()

    if not guess:
      error_msg("You have not made a guess.")
      continue

    elif not guess.isalpha():
      error_msg(f"'{guess}' is not a letter.")
      continue

    elif len(guess) > 1:
      error_msg(f"'{guess}' is invalid. Guess one letter at the time.")
      continue

    elif guess in guess_history:
      error_msg(f"You already guessed '{guess}'.")
      continue

    elif guess in chosen_word:
      pep_talk = ["Nice!", "Great!", "Excellent!", "You got it!"]
      print("\n\n" + random.choice(pep_talk))

      for position, letter in enumerate(chosen_word):
        if letter == guess:
          display[position] = letter

    else:
        lives -= 1
        print(f"\n'{guess}' is not in the mistery word.")
        print(f"You lost one live. {lives} live{'s' if lives > 1 else ''} remaining.")

    guess_history.append(guess)

  # At the end of the game
  print_stage()

  win_msg = "\nYou WIN!"
  lost_msg = f"\nYou lost, sorry... The mistery word was '{chosen_word}'."

  print(win_msg) if display == list(chosen_word) else print(lost_msg)

  play_msg = "\nWanna play again? Y or N: "

print("\nSee you another time!")