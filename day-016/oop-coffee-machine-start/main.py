## Day 16 - Coffee Machine Project | OOP Version
## 12.06.2023

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

is_machine_on = True

while is_machine_on:
    choice = input(f"What would you like? ({menu.get_items()}): ").lower()

    if choice == "off":
        is_machine_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink is not None:
            if coffee_maker.is_resource_sufficient(drink):
                payment = money_machine.make_payment(drink.cost)
                if payment:
                    coffee_maker.make_coffee(drink)
        else:
            print("Sorry, that's not a valid choice. Please try again.")