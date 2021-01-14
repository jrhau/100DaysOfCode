########################################################################
# #100DaysofCode                                      By Jonathan Rhau #
#                                                                      #
#                        Day 10 - Calculator                           #
#                                                                      #
########################################################################

from art import logo
import os

def reset_screen():
  os.system("clear") if os.name == "posix" else os.system("cls")
  print(logo + "\n")

def add(n1,n2):
  return n1+n2

def subtract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculation():
  previous_answer = None
  keep_going = True
  while(keep_going):
    reset_screen()

    # Using != to avoid case where the previous answer was 0
    if previous_answer != None:
      num1 = previous_answer
      print(f"Your previous answer was: {num1:0.2f}")
    else:
      num1 = float(input("What's the first number?: "))

    for symbol in operations:
      print(symbol)

    operation_symbol = input("Pick an operation from the above: ")
    num2 = float(input("What's the second number?: "))

    func = operations[operation_symbol]

    answer = func(num1, num2)
    print(f"\n{num1:0.2f} {operation_symbol} {num2:0.2f} = {answer:0.2f}\n")

    msg = "Type 'y' to continue from the previous answer"
    msg += "\nType 'n' for a new calculation"
    msg += "\nType return key to quit\n"

    continue_answer = input(msg).lower()

    if continue_answer == 'y':
      previous_answer = answer
    elif continue_answer == 'n':
      previous_answer = None
    else:
      keep_going = False

calculation()