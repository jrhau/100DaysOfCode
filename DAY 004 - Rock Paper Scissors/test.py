from utils import rock, paper, scissors, print_result

# Print all possibilities
choices = [rock, paper, scissors]
for p1 in range(3):
  for pc in choices:
    print_result(choices[p1], pc)
    if choices[p1] == pc:
      print("This is a DRAW!")
    elif choices[p1 -1] == pc:
      print("You WON!")
    else:
      print("You LOST!")