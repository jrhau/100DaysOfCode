########################################################################
# #100DaysofCode                                      By Jonathan Rhau #
#                                                                      #
#                         Day 11 - BlackJack                           #
#                                                                      #
########################################################################

from art import logo, hearts, spades, diamonds, clubs, hidden_face
import os

card_value = ["A"] + [str(num) for num in range(2, 11)] + ["J", "Q", "K"]
card_base = [hearts, spades, diamonds, clubs]

MAX_SCREEN_SIZE = 80


def reset_screen() -> None:
    """Clears the screen and print the game logo"""
    os.system("clear") if os.name == "posix" else os.system("cls")
    print(logo)
    print("=" * 80)


def card_factory(value: str, base: str, is_hidden: bool = False) -> str:
    """Generate a card ASCII art
    value: A, 1-10, J, Q, K
    base: hearts, spades, clubs, diamonds
    is_hidden: Card state. True or False
    """
    if 1 <= len(value) <= 2:
        card = list(base)
        card[13:15] = f"{value} " if len(value) == 1 else f"{value}"
        card[74:76] = f" {value}" if len(value) == 1 else f"{value}"
    else:
        raise Exception("Invalid value lenght. Must be 1 or 2 charaters")

    return hidden_face if is_hidden else "".join(card)


def new_deck(shoe_size=1, is_hidden=True) -> list:
    """Generating a new deck at a new memory location
    shoe_size: Number of deck to generate"""
    result = []
    for deck in range(shoe_size):
        result += [
            {"value": value, "base": base, "is_hidden": is_hidden}
            for base in card_base
            for value in card_value
        ]
    return result


def print_hand(hand: list, output: bool = True) -> str:
    """Print up to 7 cards per row
    hand: List of cards
    output: Print to screen or not
    Return: screenshot in a str format"""
    # Split each card ASCII art into lines
    hand = [card_factory(**card).split("\n") for card in hand]

    screenshot = ""
    # The max display is 80 char long, so 6 card max can fit in one row
    # We will split the hand into slices of 6 cards to print
    for row in [hand[x: x + 6] for x in range(0, len(hand), 6)]:
        # Print line x of each cards in the hand
        for line_number in range(len(hand[0])):
            # Adjusting the spacing so the cards are centered
            current_line = "     " + " " * (7 - len(row)) * 5
            for card in row:
                current_line += card[line_number] + " "

            screenshot += current_line + "\n"
            if output:
                print(current_line)

    return screenshot


def popup(
    msg: str, screen: str = None, x: int = None, y: int = None, output: bool = True
) -> str:
    """Overlay a popup message to screen.
    screen: Screen where the popup will overlay
    msg: Message to print
    x: x axis position. If None, will center horizontally on the screen
    y: y axis position, If None, will center vertically on the screen
      * popup will be center using the x,y axis position
      * if popup position to far on the right or the bottom,
        popup will be cropped
      * if popup position to far on the left or the top,
        popup will be repositionned
    output: Print to screen or not
    Return: Screenshot in a str format
    """

    box_size = {"x": 0, "y": 0}

    # Calculating the box size
    for line in msg.split("\n"):
        if len(line) > box_size["x"]:
            box_size["x"] = len(line)
        box_size["y"] += 1

    margin = {"x": 3, "y": 2}
    # Building the popup (list of list)
    popup = []
    popup.append([" ", ".", "-"] + ["-"] * box_size["x"] + ["-", ".", " "])
    popup.append([" ", "|", " "] + [" "] * box_size["x"] + [" ", "|", " "])

    for line in msg.split("\n"):
        popup.append(
            [" ", "|", " "]
            + list(line)
            + [" "] * (box_size["x"] - len(line))
            + [" ", "|", " "]
        )

    popup.append([" ", "|", " "] + [" "] * box_size["x"] + [" ", "|", " "])
    popup.append([" ", "'", "-"] + ["-"] * box_size["x"] + ["-", "'", " "])

    # If no screen was given, create a blank screen the size of the popup
    if screen is None:
        screen = [ [" "]*80 for _ in range(box_size["y"] + margin["y"]*2 + 2)]
    else:
      # Converting the msg into a list of list
      # and filling the rest of the line with white spaces
      screen = [
          list(line) + [" "] * (MAX_SCREEN_SIZE - len(line))
          for line in screen.split("\n")
      ]


    pos = {}
    pos["x"] = x if x is not None else len(screen[0]) // 2
    pos["y"] = y if y is not None else len(screen) // 2

    # Shifting the popup position if to far on the left or to high on the top
    min_x = (box_size["x"] + margin["x"]) // 2 + 1
    min_y = (box_size["y"] + margin["y"]) // 2 + 1

    pos["x"] = pos["x"] if pos["x"] >= min_x else min_x
    pos["y"] = pos["y"] if pos["y"] >= min_y else min_y

    # Start cursor cannot be lower than 0
    start = {}
    start["x"] = pos["x"] - (box_size["x"] // 2) - margin["x"]
    start["x"] = 0 if start["x"] < 0 else start["x"]
    start["y"] = pos["y"] - (box_size["y"] // 2) - margin["y"]
    start["y"] = 0 if start["y"] < 0 else start["y"]

    # End cursor position cannot be greater than the screen size
    end = {}
    end["x"] = start["x"] + box_size["x"] + margin["x"]*2
    if end["x"] > len(screen[0]):
        end["x"] = len(screen[0])

    end["y"] = start["y"] + box_size["y"] + margin["y"]*2
    if end["y"] > len(screen):
        end["y"] = len(screen) - margin["y"]

    # Overlapping the popup onto the screen
    line = 0
    for idx in range(start["y"], end["y"]+1):
        # Cropping on the y axis if too long
        if line < len(popup):
          screen[idx][start["x"]: end["x"]] = popup[line]
          line += 1

    # Cropping the excess on the x axis. Max screen size is 80 char
    for line in range(len(screen)):
        screen[line] = screen[line][0:MAX_SCREEN_SIZE]

    if output:
        for line in screen:
            print("".join(line))

    screenshot = ""
    for line in screen:
        screenshot += "".join(line) + "\n"

    return screenshot

def validated_input(input_msg: str, error_msg: str, validator, screenshot:str =None):
  """Recurse until the input data pass validation

  input_msg: Text to display when prompting for data
  error_msg: Error message to popup. 
    * You can include the data in your message with {}
      since using the .format(data) on the error msg
  validator: Function to validate the received data
    * If validation do not pass, validator function must 
      raise an Exception
  screenshot: The current screen display output. 
              The popup will overlay. 
  """
  while(True):
    reset_screen()

    if screenshot is not None:
      print(screenshot)

    data = input(input_msg)

    try:
      return validator(data)
    except:
      reset_screen()
      popup(error_msg.format(data), screenshot)
      input("")

def hand_points(hand):
  """Calulating all hand points combinaison and returning the best one
  Also return adjective or Hard or Soft depending on how the A was dealt"""
  points = [[]]
  branch = 1
  for card in hand:
    if not card["is_hidden"]:
      if card["value"].isnumeric():
        for possibility in range(branch):
          points[possibility].append(int(card["value"]))
      elif card["value"] == "A":
        for possibility in range(branch):
          # Ace is 1 or 11. Creating the two possibility
          points.append(points[possibility] + [11])  
          points[possibility].append(1)
          branch += 1
      else:
        # Left are the face value of 10
        for possibility in range(branch):
          points[possibility].append(10)

  score = list(zip([sum(branch) for branch in points], points))
  score.sort(key=lambda x: x[0], reverse=True)

  for total, points in score:
    if total == 21 and len(hand) == 2:
      return total, "BlackJack!"
    if total <= 21:
      if 1 in points and 11 in points:
        return total, None
      if 1 in points: 
        return total, "Soft"
      if 11 in points:
        return total, "Hard"
      else:
        return total, None

  # If you get there, you have lost or you had empty hand 
  # or all card in hand was hiddien
  if score:
    return score[-1][0], None
  else:
    return 0, None