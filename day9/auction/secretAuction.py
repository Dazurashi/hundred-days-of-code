'''
    This program takes in user name and their bid.
    Then the program asks if there are any other people joining the auction.
    If there are other people, console is cleared so the next person doesn't see the previous bid.
    Finally when there are no more people joining, winner with highest bid is printed.
'''

import os
from art import logo
print(logo)

people = {}

while True:
    name = input("Name: ")
    bid = input("Bid: $")
    people[name] = bid
    #print(people)
    answer = input("Are there more people? Answer yes or no: ").lower()
    if answer == "yes":
        os.system("clear")
        continue
    else:
        break

highestBid = max(people)
print(f"Highest bid was from {highestBid} with ${people[highestBid]}")