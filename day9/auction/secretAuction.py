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