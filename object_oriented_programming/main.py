from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


profit = MoneyMachine()
resources = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"what would you like ({options})")

    if choice == "off":
        is_on = False
    elif choice == "report":
        resources.report()
        profit.report()
    else:
        drinks = menu.find_drink(choice)
        print(drinks)
        if resources.is_resource_sufficient(drinks) and profit.make_payment(drinks.cost):
            resources.make_coffee(drinks)
