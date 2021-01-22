########################################################################
# #100DaysofCode                                      By Jonathan Rhau #
#                                                                      #
#                      Day 15 - Coffee Machine                         #
#                                                                      #
########################################################################
import os

LOGO = """
   _____       __  __            __  __            _     _            
  / ____|     / _|/ _|          |  \/  |          | |   (_)           
 | |     ___ | |_| |_ ___  ___  | \  / | __ _  ___| |__  _ _ __   ___ 
 | |    / _ \|  _|  _/ _ \/ _ \ | |\/| |/ _` |/ __| '_ \| | '_ \ / _ \\
 | |___| (_) | | | ||  __/  __/ | |  | | (_| | (__| | | | | | | |  __/
  \_____\___/|_| |_| \___|\___| |_|  |_|\__,_|\___|_| |_|_|_| |_|\___|
                                                             
"""

ESPRESSO = """
  .-=-.
 ,|`~'|
 `|   |  ESPRESSO
   `~'
"""

LATTE = """
  .=%%=.
,|`=%%='|
||      |
`|      |  LATTE
  `-__-'
"""

CAPPUCCINO = """
  .-~~-.
,|`-__-'|
||      |
`|      |  CAPPUCCINNO
  `-__-'
"""

DRINK_ART = {
    "espresso": ESPRESSO,
    "latte": LATTE,
    "cappuccino": CAPPUCCINO
}

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
    "intake": 0
}


def reset_screen() -> None:
    """Clears the screen and print the game logo"""
    os.system("clear") if os.name == "posix" else os.system("cls")
    print(LOGO)
    print("=" * 80)


def help():
    """Display the available commands"""
    print("*"*40)
    print("The available commands are:\n")
    print("'Report'        \tDisplay the Coffee Machine ressorce levels.\n")
    print("'Menu'          \tDisplay the menu.\n")
    print("'Insert'        \tInsert coins into the machine.\n")
    print("'Order < Item >'\tRequest an item on the menu.\n")
    print("'Return'        \tReturns the change in the Coffee Machine intake.\n")
    print("'Refill'        \tReplenish the Coffee Machinne resources.\n")
    print("'Quit'          \tExit the Coffee Machine.\n")
    print("*"*40)


def menu():
    """Display the items on the menu."""
    print("*"*40)
    [print(f"{item :>10}: {MENU[item]['cost']:0.2f}$") for item in MENU]
    print("*"*40)


def calculate_coins(penny: int = 0, nickel: int = 0, dime: int = 0, quarter: int = 0) -> float:
    """Return the total value base on the coins received"""
    return penny*0.01 + nickel*0.05 + dime*0.1 + quarter*0.25


def report() -> None:
    """Print a status report on how much ressource is left"""
    print("*"*40)
    print("The current resources level are: \n")
    print(f"{'Water:':>8} {resources['water']:>03}ml")
    print(f"{'Milk:':>8} {resources['milk']:>03}ml")
    print(f"{'Coffee:':>8} {resources['coffee']:>03}g")
    print(f"{'Money:':>8} {resources['money']:0.2f}$")
    print(f"{'Intake:':>8} {resources['intake']:0.2f}$")
    print("*"*40)


def verify_resources(water: int = 0, milk: int = 0, coffee: int = 0) -> bool:
    """Verify if the coffee machine has enough resources"""
    return all([
        water <= resources["water"],
        milk <= resources["milk"],
        coffee <= resources["coffee"]
    ])


def order(item: str) -> float:
    """Process an order and return the change"""

    # Checking if the drink requested is on the menu
    drink = MENU.get(item)

    if drink:
        # Enough money?
        if resources['intake'] >= drink["cost"]:
            # Enough resources?
            if verify_resources(**drink["ingredients"]):
                # Debit resources and return change
                for k, v in drink["ingredients"].items():
                    resources[k] -= v

                resources["money"] += drink["cost"]
                resources['intake'] -= drink["cost"]

                print("")
                print(DRINK_ART[item])
                print(f"Enjoy your {item}!")

                # Propose option to return the change now.
                # Or the customer can continue to order
                if resources['intake'] > 0:
                    change = input(
                        "\nReturn your change now? Y or N: ").lower()

                    if change == "y":
                        print(f"Your change: {resources['intake']:0.2f}$")
                        resources['intake'] = 0
                    else:
                        print(
                            f"You have {resources['intake']:0.2f}$ in the intake left.")

            else:
                print(f"Not enough resources left to make your {item}.")
                print("Use the 'Refill' command to add resources.")
        else:
            print(f"{drink['cost'] - resources['intake']:0.2f}$ missing.")
    else:
        print(f"'{item}' is not on the menu.")


def insert_coins() -> dict:
    """Capturing user coins for purchase."""
    try:
        print("\nPlease, insert your coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))

        if quarters < 0 or dimes < 0 or nickels < 0 or pennies < 0:
            raise Exception("Value too low.")

        coins = {
            "penny": pennies,
            "nickel": nickels,
            "dime": dimes,
            "quarter": quarters
        }
        
        resources["intake"] += calculate_coins(**coins)
        print(f"\nThe intake now contains {resources['intake']:0.2f}$")
    except:
        print("Each coins must be a positive integer.")


def refill_resources() -> dict:
    """Replenish the Coffee Machine resources"""
    try:
        print("\nPlease, insert your coins.")
        water = int(input("How many ml of water?: "))
        milk = int(input("How many ml of milk?: "))
        coffee = int(input("How many g of coffee?: "))
        collect = input("Collect the Coffee Machine money? Y or N: ").lower()

        if water < 0 or milk < 0 or coffee < 0:
            raise Exception("Value too low. Must be positive integer")

        resources["water"] += water
        resources["milk"] += milk
        resources["coffee"] += coffee

        if collect == "y":
            print(
                f"\nYou have collected {resources['money']:0.2f}$ from the Coffee Machine.")
            resources["money"] = 0

        print("")
        report()
    except:
        print("You have to enter a positive whole number.")


def return_change():
    """Returning the accumulated money of the Coffee Machine intake bin."""
    print(f"Returning {resources['intake']:0.2f}$")
    resources["intake"] = 0


# Mapping the commands to the appropriate functions
commands = {
    "report": report,
    "menu": menu,
    "order": order,
    "insert": insert_coins,
    "return": return_change,
    "refill": refill_resources,
    "help": help
}

# Basic Coffee Machine CLI engine
reset_screen()
help()
while((cmd := input("\nEnter your command: ")).lower() != "quit"):
    reset_screen()
    cmd = cmd.split()

    if cmd:
        action = commands.get(cmd[0])
        if action:
            action(cmd[1]) if len(cmd) == 2 else action()
        else:
            print(
                f"'{' '.join(cmd)}' is not valid.\nSee 'help' for commands available.")

print("Have a wonderful day!")
