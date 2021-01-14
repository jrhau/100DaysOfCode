########################################################################
# #100DaysofCode                                      By Jonathan Rhau #
#                                                                      #
#                       Day 8 - Caesar Cipher                          #
#                                                                      #
########################################################################

from art import logo
import os

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def reset_screen():
  os.system("clear") if os.name == "posix" else os.system("cls")
  print(logo + "\n")

def caesar(text, shift, cipher_direction="encode"):
  # Remove the extra to get a number between 0 and len(alphabet)
  shift %= len(alphabet)

  if cipher_direction == "decode":
    shift *= -1

  result = ""
  for char in text:
    if char.isalpha():
      # Using % here to avoid index error if the new shifted position
      # is greater than the size of the alphabet list
      result += alphabet[(alphabet.index(char) + shift) % len(alphabet)]
    else:
      result += char
    
  print("\n" + "-"*40 + f"\n\nHere's the {cipher_direction}d result:")
  print(f"\t{result}\n")

def executor(restart=True):
  if restart:
    reset_screen()

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n\t")
    text = input("\nType your message:\n\t").lower()
    shift = int(input("\nType the shift number:\n\t"))

    caesar(text, shift, direction)

    # Recall itself if user wanna continue
    executor(input("\n Wanna cipher again? Y or N: ").lower()=="y")

############# MAIN ############
reset_screen() 
executor()