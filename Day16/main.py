import sys
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffe = CoffeeMaker()
mon =MoneyMachine()

while True:
    prompt = input(f"what would you like to drink{menu.get_items()}")
    if prompt == "off":
        print("shutting down")
        sys.exit()
    elif prompt == "report":
        coffe.report()
        mon.report()
    elif coffe.is_resource_sufficient(menu.find_drink(prompt)):
        drinks = menu.find_drink(prompt)
        if mon.make_payment(drinks.cost):
            coffe.make_coffee(drinks)






