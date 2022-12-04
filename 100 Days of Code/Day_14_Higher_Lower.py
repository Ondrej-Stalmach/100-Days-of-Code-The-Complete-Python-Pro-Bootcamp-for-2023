logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

import random
import os
from Day_14_Higher_Lower_data import data
os.system("cls")
print(logo)

num1 = random.randint(0,len(data)-1)
info1 = [data[num1]["name"], data[num1]["description"], data[num1]["country"], data[num1]["follower_count"]]
state = True
score = 0

while state:

    num2 = random.randint(0,len(data)-1)
    if num1 == num2:
        num2 = random.randint(0,len(data)-1)

    info2 = [data[num2]["name"], data[num2]["description"], data[num2]["country"], data[num2]["follower_count"]]

    print(f"Compare A: {info1[0]}, {info1[1]}, from {info1[2]}.")
    print(vs)
    print(f"Against B: {info2[0]}, {info2[1]}, from {info2[2]}.")

    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    if answer == 'a':
        if info1[3] > info2[3]:
            os.system("cls")
            print(logo)
            score = score + 1
            print(f"You're right! Current score: {score}.")
            info1 = info2
        else:
            os.system("cls")
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}.")
            state = False

    elif answer == 'b':
        if info2[3] > info1[3]:
            os.system("cls")
            print(logo)
            score = score + 1
            print(f"You're right! Current score: {score}.")
            info1 = info2
        else:
            os.system("cls")
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}.")
            state = False
    else:
        os.system("cls")
        print(logo)
        print(f"Bad choice! Only 'A' or 'B' are available.\nGame Over!")
        state = False