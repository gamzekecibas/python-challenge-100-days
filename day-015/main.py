## Day 15 - Coffee Machine Project
## 11.06.2023

## STARTER CODE ##

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
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

####

def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

def check_resources(drink):
    for ingredient, quantity in MENU[drink]['ingredients'].items():
        if resources[ingredient] < quantity:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickels = int(input("How many nickels?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    return quarters + dimes + nickels + pennies

def check_transaction_successful(drink, payment):
    if payment < MENU[drink]['cost']:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    change = round(payment - MENU[drink]['cost'], 2)
    resources['money'] += MENU[drink]['cost']
    if change > 0:
        print(f"Here is ${change} in change.")
    return True

def make_coffee(drink):
    for ingredient, quantity in MENU[drink]['ingredients'].items():
        resources[ingredient] -= quantity
    print(f"Here is your {drink}. Enjoy!☕")

is_machine_on = True

while is_machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        is_machine_on = False
    elif choice == "report":
        print_report()
    elif choice in MENU:
        if check_resources(choice):
            payment = process_coins()
            if check_transaction_successful(choice, payment):
                make_coffee(choice)
    else:
        print("Sorry, that's not a valid choice. Please try again.")