logo = """
   _____       __  __            __  __            _     _            
  / ____|     / _|/ _|          |  \/  |          | |   (_)           
 | |     ___ | |_| |_ ___  ___  | \  / | __ _  ___| |__  _ _ __   ___ 
 | |    / _ \|  _|  _/ _ \/ _ \ | |\/| |/ _` |/ __| '_ \| | '_ \ / _ |
 | |___| (_) | | | ||  __/  __/ | |  | | (_| | (__| | | | | | | |  __/
  \_____\___/|_| |_| \___|\___| |_|  |_|\__,_|\___|_| |_|_|_| |_|\___|
"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "machine": {
        
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "money": 0.0
    }
}

import os


def report():
    info = "\nCoffe Machine Info:\nWatter: " + str(MENU["machine"]["water"]) + "ml\nMilk: " + str(MENU["machine"]["milk"]) + "ml\nCoffe: " + str(MENU["machine"]["coffee"]) + "g\nMoney: $" + str(MENU["machine"]["money"])
    print(info)


def check_ingrediens():
    if MENU[type_of_coffee]["ingredients"]["water"] > MENU["machine"]["water"]:
        return "Sorry there is not enough water. "
    elif MENU[type_of_coffee]["ingredients"]["milk"] > MENU["machine"]["milk"]:
        return "Sorry there is not enough milk. "
    elif MENU[type_of_coffee]["ingredients"]["coffee"] > MENU["machine"]["coffee"]:
        return "Sorry there is not enough coffee. "
    else:
        return "OK"


def calculation(quarters,dimes,nickles,pennies):
    income = (0.25*quarters) + (0.1*dimes) + (0.05*nickles) + (0.01*pennies)
    cost = MENU[type_of_coffee]["cost"]
    outcome = round(income - cost,2)

    if income >= cost and check_ingrediens() == "OK":
        print(f"Here is ${outcome} in change.")
        print(f"Here is your {type_of_coffee} ☕ Enjoy!")
        machine_options(income)
        return True
    elif check_ingrediens() != "OK":
        print(check_ingrediens() + f"${income} refunded.")
        return False
    else:
        print(f"Sorry that's not enough money. ${income} refunded.")
        return True


def machine_options(income):
    MENU["machine"]["water"] = MENU["machine"]["water"] - MENU[type_of_coffee]["ingredients"]["water"]
    MENU["machine"]["milk"] = MENU["machine"]["milk"] - MENU[type_of_coffee]["ingredients"]["milk"]
    MENU["machine"]["coffee"] = MENU["machine"]["coffee"] - MENU[type_of_coffee]["ingredients"]["coffee"]
    MENU["machine"]["money"] = MENU["machine"]["money"] + income


state = True
os.system("cls")
print(logo)

while state:
    
    type_of_coffee = input("\nWhat would you like? espresso ($1.5)/ latte ($2.5)/ cappuccino ($3.0): ").lower()
    if type_of_coffee == "report":
        report()
    elif type_of_coffee == "off":
        print("Turn off Coffee Machine")
        state = False
    else:
        print("Please insert coins.")
        quarters = int(input("How many quarters? "))
        dimes = int(input("How many dimes? "))
        nickles = int(input("How many nickles? "))
        pennies = int(input("How many pennies? "))
        print("\n")
        state = calculation(quarters,dimes,nickles,pennies)
        
       


