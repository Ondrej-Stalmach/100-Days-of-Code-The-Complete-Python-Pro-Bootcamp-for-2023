from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_machine = CoffeeMaker()
menu = Menu()

# coffee_machine.report()
# money_machine.report()

print(menu.get_items())

state = True
while state:
    type_of_coffee = input(f"\nWhat would you like? {menu.get_items()}: ").lower()
    if type_of_coffee == "off":
        print("\n")
        print("Turn Off Coffee Machine")
        state = False
    elif type_of_coffee == "report":
        print("\n")
        coffee_machine.report()
        money_machine.report()
    else:
        drink = menu.find_drink(type_of_coffee)
        if coffee_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)
