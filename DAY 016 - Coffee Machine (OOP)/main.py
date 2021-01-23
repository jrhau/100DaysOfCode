########################################################################
# #100DaysofCode                                      By Jonathan Rhau #
#                                                                      #
#                    Day 16 - Coffee Machine (OOP)                     #
#                                                                      #
########################################################################

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cm = CoffeeMaker()
mm = MoneyMachine()
menu = Menu()
is_on = True
while is_on:

    choice = input("What would you like? (espresso/latte/cappuccino/): ").lower()

    if choice == "off":
        is_on = False
    if choice == "report":
        cm.report()
        mm.report()
    if choice in ["espresso", "latte", "cappuccino"]:
        drink = menu.find_drink(choice)
        if cm.is_resource_sufficient(drink):
            if mm.make_payment(drink.cost):
                cm.make_coffee(drink)
