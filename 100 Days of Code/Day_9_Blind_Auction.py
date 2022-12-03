logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

import os
print(logo)
print("\nWelcome to the secrete auction program.")

def find_highest_bid(dictionary):
    highest_bid = 0
    winner = ""
    for key in dictionary:
        bid_value = dictionary[key]
        if bid_value > highest_bid:
            highest_bid = bid_value
            winner = key
    print(f"\nThe winner is {winner} with a bid of ${highest_bid}")
        

auction = {}
state = True

while state:

    get_name = input("What is your name? ")
    get_bid = int(input("What's your bid? $"))
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no' . ").lower()

    auction[get_name ] = get_bid
    

    if other_bidders == 'no':
        find_highest_bid(auction)
        state = False
        print("\nGame Over")
        
    elif other_bidders == 'yes':
        os.system("cls")
    else:
        state = False
        print("\nYou had to type 'yes' or 'no'! \nGame Over")

