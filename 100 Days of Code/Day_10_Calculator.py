logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

import os

def add(num1, num2):
    return num1 + num2

def subtract(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    return num1 / num2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide    
}
def calculator():
    print(logo)

    number1 = float(input("What's the first number? "))
    state = True
    for key in operations:
        print(key)

    while state:    
        operation_symbol = input("Pick an operation symbol: ")
        number2 = float(input("What's the next number? "))

        calculation = operations[operation_symbol]
        result = calculation(number1,number2)
        print(f"{number1} {operation_symbol} {number2} = {result}")
        ask = input(f"Type 'y' to continue calculation with {result}, or type 'n' for new calculation or 'q' to end: ")
        if ask == 'y':
            number1 = result
        elif ask == 'n':
            state = False
            os.system("cls")
            calculator()
        else:
            state = False
            print("\nThank you and have a nice day.")

calculator()