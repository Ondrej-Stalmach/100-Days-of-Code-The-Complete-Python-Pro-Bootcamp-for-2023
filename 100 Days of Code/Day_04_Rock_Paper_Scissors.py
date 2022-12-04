rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
computer = random.randint(0,2)

options = [rock,paper,scissors]

if choice == 0 and computer == 1:
    print("You chose:")
    print(options[choice])
    print("Computer chose:")
    print(options[computer])
    print("You lose") 
elif choice == 1 and computer == 2:
    print("You chose:")
    print(options[choice])
    print("Computer chose:")
    print(options[computer])
    print("You lose") 
elif choice == 2 and computer == 0:
    print("You chose:")
    print(options[choice])
    print("Computer chose:")
    print(options[computer])
    print("You lose") 
elif choice==computer:
    print("You chose:")
    print(options[choice])
    print("Computer chose:")
    print(options[computer])
    print("It's a draw") 
elif choice>2 or choice<0:
    print("Bad choice! Insert 0, 1 or 2.")
else:
    print("You chose:")
    print(options[choice])
    print("Computer chose:")
    print(options[computer])
    print("You Win!") 




