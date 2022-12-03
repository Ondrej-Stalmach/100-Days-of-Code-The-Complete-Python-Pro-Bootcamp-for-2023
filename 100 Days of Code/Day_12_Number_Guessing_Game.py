logo = """
  _   _                 _                  _____                     _                _____                      
 | \ | |               | |                / ____|                   (_)              / ____|                     
 |  \| |_   _ _ __ ___ | |__   ___ _ __  | |  __ _   _  ___  ___ ___ _ _ __   __ _  | |  __  __ _ _ __ ___   ___ 
 | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | |_ | | | |/ _ \/ __/ __| | '_ \ / _` | | | |_ |/ _` | '_ ` _ \ / _ 
 | |\  | |_| | | | | | | |_) |  __/ |    | |__| | |_| |  __/\__ \__ \ | | | | (_| | | |__| | (_| | | | | | |  __/
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \_____|\__,_|\___||___/___/_|_| |_|\__, |  \_____|\__,_|_| |_| |_|\___|
                                                                              __/ |                              
                                                                             |___/                               
"""

import random
import os
os.system("cls")
print(logo)
print("\nWelcome to the Number Guessing Game!")

state = True
print("I'm thinking of a number between 1 and 100.")
secret_number = random.randint(1,100)
type = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if type == 'easy':
    lives = 10
elif type == "hard":
    lives = 5
else:
    print("Only 'easy' or 'hard' mode are available!")
    state = False

while state:
    
    print(f"\nYou have {lives} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == secret_number:
        print(f"You win guessed number was {secret_number}")
        state = False
    elif lives == 0:
        print(f"You lose.")
        state = False
    elif guess > secret_number:
        print("Too high.\nGuess again.")
        lives = lives - 1
    elif guess < secret_number:
        print("Too low.\nGuess again.")
        lives = lives - 1