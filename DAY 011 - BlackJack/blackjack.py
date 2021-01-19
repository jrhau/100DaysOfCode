########################################################################
# #100DaysofCode                                      By Jonathan Rhau #
#                                                                      #
#                         Day 11 - BlackJack                           #
#                                                                      #
########################################################################

from utils import reset_screen, new_deck, print_hand, hand_points, popup, validated_input
import random, time


def blackjack_engine():
######################## Internal variable init ################################

  game = {}
  game["settings"] = {}
  game["settings"]["bank"] = {}
  game["settings"]["bank"]["min"] = 50
  game["settings"]["bank"]["max"] = 100000
  game["settings"]["bank"]["init"] = 1000

  game["settings"]["shoe"] = {}
  game["settings"]["shoe"]["min"] = 1
  game["settings"]["shoe"]["max"] = 6
  game["settings"]["shoe"]["size"] = 1

  game["settings"]["display"] = {}
  game["settings"]["display"]["points"] = True

  game["deck"] = []
  
  player = {}  
  dealer = {}
  player["header"] = "Your hand:"
  player["hand_name"] = ["first", "second", "third", "forth", "fifth", "sixth"]
  dealer["header"] = "Dealer's hand:"
########################### Internal functions #################################
  
  # Validator functions are pluggins for the validated_input function.
  # If validation fails, the validator functions must raise an error
  
  def validate_bank_init_amount(data):
    if data == "":
      return game["settings"]["bank"]["init"]
    
    data = int(data)
    
    if game["settings"]["bank"]["min"] <= data <= game["settings"]["bank"]["max"]:
      return data
    else:
      raise Exception(f"'{data}' not in the range settings-bank-min/max") 
    
  def validate_shoe_size(data):
    if data == "":
      return game["settings"]["shoe"]["size"]
    
    data = int(data)
    if game["settings"]["shoe"]["min"] <= data <= game["settings"]["shoe"]["max"]:
      return data
    else:
      raise Exception(f"'{data}' not in the range settings-shoe-min/max") 
    
  def validate_show_points(data):
    if data == "":
      return game["settings"]["display"]["points"]
        
    data = data.lower()
    
    if data in ["y", "n"]:
      return data == "y"
    else:
      raise Exception("Must be 'y' or 'n' or ''.")
    
  def validate_decision(data):
    data = data.lower()
    choice = {"h":"hit", "s":"split", "d":"double", "":"stand"}
  
    if data in ["h", "s", "d", ""]:
        return choice[data]
    else:
        raise Exception("Must be 'h', 's', 'd', or ''")
  
  def validate_bet(data):
    if data == "":
      return data  
    data = int(data)  
    if 1 <= data <= player["bank"]:
      return data
    else:
      raise Exception(f"Must be between 1 and {player['bank']}")

  # ------------------------------------------------------------------------ #
 
  def print_status_line(msg:str, status:str, output:bool=True)->str:
    """Print msg on the left and status on the right""" 
    status_line = msg + " "*(80-len(msg)-len(status)) + status  
    if output:
      print(status_line)  
    return status_line + "\n"

  def print_screen(hand_number:int=None, output:bool=True)->str:
    """Print Dealer's and Player's hand"""
    reset_screen()
    screen = print_status_line(
        msg="",
        status=f"Cards left: {len(game['deck'])}",
        output=False
    )
    screen += dealer["header"] + "\n"
    for hand in dealer["hand"]:
      if game["settings"]["display"]["points"]:
        points, adjective = hand_points(hand)
        screen += f"    POINTS: {points} {adjective if adjective else ''}\n"
      screen += print_hand(hand, output=False)

    screen += "\n" + " "*20 + "-"*40 + " "*20 + "\n"

    if hand_number is None:
      for idx, (hand, bet) in enumerate(zip(player["hand"], player["bet"])):
        header = player["header"] if len(player["hand"]) == 1 else f"Your {player['hand_name'][idx]} hand:"
        bank_info = f"BANK: ${player['bank']}" if idx == 0 else ""

        screen += print_status_line(msg=header, status=bank_info, output=False)

        if game["settings"]["display"]["points"]:
          points, adjective = hand_points(hand)
          screen += f"    POINTS: {points} {adjective if adjective else ''}\n"
        screen += f"    BET: ${bet}\n"
        screen += print_hand(hand, output=False)
    else:
      hand, bet = player["hand"][hand_number], player["bet"][hand_number]  
      header = player["header"] if len(player["hand"]) == 1 else f"Your {player['hand_name'][hand_number]} hand:"
      screen += print_status_line(msg=header, status=f"BANK: ${player['bank']}", output=False)
      if game["settings"]["display"]["points"]:
        points, adjective = hand_points(hand)
        screen += f"    POINTS: {points} {adjective if adjective else ''}\n"
      screen += f"    BET: ${bet}\n"
      screen += print_hand(hand, output=False)

    if output:
      print(screen)

    return screen

  def decision(hand:list, bet:int, screenshot:str=None)->str:
    """Display and capture a player's decision for a specific hand"""
    points, _ = hand_points(hand)

    if points < 21:

      choices = {}
      choices["hit"] = True
      choices["stand"] = True
      choices["double"] = False
      choices["split"] = False

      if len(hand) == 2 and bet <= player["bank"]:
        choices["double"] = True

        possibility = ["10", "J", "Q", "K"]
        choices["split"] =  hand[0]["value"] == hand[1]["value"] or all(card in possibility for card in hand)

      msg = ""
      if choices["hit"]:
        msg += "[H] Hit\n"
      if choices["double"]:
        msg += "[D] Double\n"
      if choices["split"]:
        msg += "[S] Split\n"
      if choices["stand"]:
        msg += "[Return Key] to Stand"  
  
      while(True):
        choice = validated_input(
          input_msg="What will you do? Select from the above: ",
          error_msg="'{}' is an invalid option",
          validator=validate_decision,
          screenshot=popup(msg, screenshot, output=False)
        )  
  
        # Player must choose among the presented option
        if choices[choice]:
          return choice
        else:
          reset_screen()
          popup(f"'{choice}' is not among your possible option.", screenshot)
          input("Continue...")
    else:
      # If player has a BlackJack or has busted
      return "stand"

############################ Game Launch #######################################

  reset_screen()

  # First run messages
  play_msg = "Wanna play a game of Blackjack? Y or N: "
  setting_msg = "Wanna change the game initial settings? Y or N: "

  while(input(play_msg).lower() == "y"):
    # next run message
    play_msg = "Wanna play another game of Blackjack? Y or N: "
    reset_screen()

    msg  = "               The game screen size is 80 characters large.\n\n"
    msg += "<----------- Please, adjust your terminal window accordingly. ------------>\n\n"
    msg += "                                  Enjoy!"

    popup(msg)

########################## Game Settings section ###############################

    if input(setting_msg).lower() == "y":
      while(True):
        msg  = "Bank amount: ${}\n"
        msg += "Shoe Size:   {} Deck\n"
        msg += "Show points: {}"

        reset_screen()
        game["settings"]["bank"]["init"] = validated_input(
          input_msg="Bank amount: $", 
          error_msg="'{}' is invalid.\nMust be a whole number\nbetwwen 50 and 100000...", 
          validator=validate_bank_init_amount,
          screenshot=popup(msg.format(
              game["settings"]["bank"]["init"], 
              game["settings"]["shoe"]["size"], 
              'Y' if game["settings"]["display"]["points"] else 'N'))
        )

        reset_screen()
        game["settings"]["shoe"]["size"] = validated_input(
          input_msg="Shoe size: ", 
          error_msg="'{}' is invalid.\nMust be a whole number\nbetwwen 1 and 6...", 
          validator=validate_shoe_size,
          screenshot=popup(msg.format(
              game["settings"]["bank"]["init"], 
              game["settings"]["shoe"]["size"], 
              'Y' if game["settings"]["display"]["points"] else 'N'))
        )

        reset_screen()
        game["settings"]["display"]["points"] = validated_input(
          input_msg="Show points? Y or N: ", 
          error_msg="'{}' is invalid.\nMust be a 'y' or 'n'.", 
          validator=validate_show_points,
          screenshot=popup(msg.format(
              game["settings"]["bank"]["init"], 
              game["settings"]["shoe"]["size"], 
              'Y' if game["settings"]["display"]["points"] else 'N'))
        )

        # reset screen and show popup with updated values for confirmation
        reset_screen()
        popup(msg.format(
              game["settings"]["bank"]["init"], 
              game["settings"]["shoe"]["size"], 
              'Y' if game["settings"]["display"]["points"] else 'N')
        )

        if input("Are you ok with those? Y or N: ").lower() != "n":
          # next run message
          setting_msg = "Wanna change your previous game settings? Y or N: "
          break

################################################################################
    
    # Applying game init settings      
    player["bank"] = game["settings"]["bank"]["init"]
    game["deck"] = new_deck(game["settings"]["shoe"]["size"])

    # Magic number to determine when the shoe should be replenish
    blank_card = random.randint(10, game["settings"]["shoe"]["size"]*15)

############################# Game Round #######################################

    round_number = 1
    while(True):
      if player["bank"] <= 0:
        reset_screen()
        popup("You are broke! You can't play anymore")
        input("I understand...")
        break

      if len(game["deck"]) <= blank_card:
        game["deck"] = new_deck(game["settings"]["shoe"]["size"])
        blank_card = random.randint(10, game["settings"]["shoe"]["size"]*15)
        reset_screen()
        msg  = "A blank card has been drawn in the previous round.\n"
        msg += "            The shoe has be replenish"
        popup(msg)
        input("Continue...")

      random.shuffle(game["deck"])
  
      reset_screen()
      print_status_line(f"Round # {round_number}", "Shuffling!")
      
      time.sleep(1)
  
      dealer["hand"] = [[game["deck"].pop(), game["deck"].pop()]]
      player["hand"] = [[game["deck"].pop(), game["deck"].pop()]]
      player['bet'] = [0]
      player["deal_again"] = [True]


      # Player cycle
      possible_play_left = True
      while(possible_play_left):
        possible_play_left = any(player["deal_again"])
        for idx, (hand, bet) in enumerate(zip(player["hand"], player["bet"])):
          # Allow to bet even if the 'deal_again' flag is not set
          if not bet:
            bet = proposed_bet = 100 if player["bank"] > 100 else player["bank"] // 2
          
            bet = validated_input(
              input_msg=f"How much will you bet? ",
              error_msg="'{}' is not valid.\nYour bet must be between $1 and" + f" ${player['bank']}",
              validator=validate_bet,
              screenshot=popup(f"Bet ${bet} ?", print_screen(idx, output=False), output=False)
            )
          
            if bet == "":
              bet = proposed_bet
      
            player['bank'] -= bet         
            player['bet'][idx] = bet

          if player["deal_again"][idx]:
            screen = print_screen(idx)
        
            # Reveal one card of the dealer's hand
            if dealer["hand"][0][0]["is_hidden"]:
              dealer["hand"][0][0]["is_hidden"] = False
              time.sleep(1)
  
            # Reveal all the cards of the player's hand(s)
            for card_num in range(len(player["hand"][idx])):
              if player["hand"][idx][card_num]["is_hidden"]:
                screen = print_screen(idx)
                time.sleep(1)
                player["hand"][idx][card_num]["is_hidden"] = False
                

            screen = print_screen(idx)
            time.sleep(1)
  

            points, adjective = hand_points(hand)
            if points == 21 and adjective == "BlackJack!":
              reset_screen()
              popup("BlackJack!", screen, y=23)
              input("Continue...")
            elif points > 21:
              reset_screen()
              popup("  Busted  ", screen, y=23)
              input("Continue...")

            # Making a decision
            choice = decision(player["hand"][idx], player["bet"][idx], screen)
        
            screen = print_screen(idx)
        
            # Applying the decision
            if choice == "hit":
              player["hand"][idx].append(game["deck"].pop())
              player["deal_again"][idx] = True
            elif choice == "double":
              while(True):
                bet = player['bet'][idx]

                popup_screen = popup(f"Add ${bet} ?", screen, output=False)

                bet = validated_input(
                  input_msg=f"How much will you add to your previous bet? $",
                  error_msg="'{}' is not valid.\nYour bet must be between $1 and" + f" ${player['bet'][idx]}",
                  validator=validate_bet,
                  screenshot=popup_screen
                )
                if bet == "":
                  bet = player['bet'][idx]
                

                if bet <= player['bet'][idx]:
                  break
                else:
                  reset_screen()
                  popup("Your bet must be between $1 and"+f" ${player['bet'][idx]}", popup_screen)
                  input("Continue...")

              player["hand"][idx].append(game["deck"].pop())
              player["bank"] -= bet
              player["bet"][idx] += bet
              player["deal_again"][idx] = True
            elif choice == "split":
              # Remove the duplicated card from the current hand
              card = player["hand"][idx].pop()
              print_screen()
              time.sleep(1)

              # Add the duplicated card to a new hand and a corresponding bet 
              player["hand"].append([card])
              player["bet"].append(bet)
              player["bank"] -= player["bet"][idx]
              print_screen()
              time.sleep(1)

              # Add a new card to the current hand
              player["hand"][idx].append(game["deck"].pop())
              print_screen()
              time.sleep(1)

              # Add a new card to the new hand
              player["hand"][-1].append(game["deck"].pop())
              screen = print_screen()
              time.sleep(1)
              
              # If the duplicated cards were Aces, not allow to deal more
              player["deal_again"][idx] = card["value"] != "A"
              player["deal_again"].append(card["value"] != "A")

              if card["value"] == "A":
                popup("   When slipping a pair of Aces\nYou are not allowed to hit again.", screen, y=20 + 10*(len(player["hand"])-1))
              input("Continue with one hand at time...")
              break #So we can restart the for loop with the updated hand list
            elif choice == "stand":
              player["deal_again"][idx] = False

            screen = print_screen(idx)
            time.sleep(1)


      # Reveal all the cards of the player's hand(s) if left hidden
      for idx in range(len(player["hand"])):
        for card_num in range(len(player["hand"][idx])):
          if player["hand"][idx][card_num]["is_hidden"]:
            print_screen()
            time.sleep(1)
            player["hand"][idx][card_num]["is_hidden"] = False

      print_screen()
      input("End of your plays. Continue...")

      # Dealer's cycle
      print_screen(0)
      time.sleep(1)
      dealer["hand"][0][1]["is_hidden"] = False
      print_screen(0)
      time.sleep(1)

      while(hand_points(dealer["hand"][0])[0] < 17):
        dealer["hand"][0].append(game["deck"].pop())
        print_screen(0)
        time.sleep(1)
        dealer["hand"][0][-1]["is_hidden"] = False
        print_screen(0)
        time.sleep(1)


      dealer_points = hand_points(dealer["hand"][0])[0]

      # Win or Loss cycle
      for idx, (hand, bet) in enumerate(zip(player["hand"], player["bet"])):
        print_screen(idx)
        time.sleep(1)
        
        player_points = hand_points(hand)[0]

        if player_points > 21:
          # Showing two popup
          screen = print_screen(idx, output=False)
          screen = popup(f"You lost ${bet}", screen, y=23, output=False)
          popup("Dealer Win", screen, y=8)
        elif player_points == dealer_points:
          # Returning the bet into player's bank
          player["bank"] += bet
          popup("Draw", print_screen(idx, output=False), y=15)
        elif player_points == 21 and len(hand) == 2:
          # Win 150%. Using x + x//2 instead of x*1.5 to avoid fractions
          player["bank"] += bet + bet + bet//2

          # Showing two popup
          screen = print_screen(idx, output=False)
          screen = popup(f"BlackJack!: You win ${bet+bet//2}!", screen, y=23, output=False)
          popup("Dealer Lost", screen, y=8)
        elif player_points > dealer_points or dealer_points > 21:
          player["bank"] += bet*2

          # Showing two popup
          screen = print_screen(idx, output=False)
          screen = popup(f"You Win ${bet}", screen, y=23, output=False)
          popup("Dealer Lost", screen, y=8)
        else:
          # Showing two popup
          screen = print_screen(idx, output=False)
          screen = popup(f"You lost ${bet}", screen, y=23, output=False)
          popup("Dealer Win", screen, y=8)
        
        # Pause for player analysis
        input("Continue...")
    

      print_screen()
      if input("Wanna play another round? Y or N: ").lower() == "n":
        break

      round_number += 1

  reset_screen()
  print("See you next time!")

# Running the app
blackjack_engine()
