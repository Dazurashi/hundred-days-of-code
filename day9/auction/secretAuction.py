from art import logo
print(logo)

people = {}

#TODO find the highest bid if there's no other people entering the auction
#TODO clear the console if there are more people so the next one doesn't see how much the previous bid

while True:
    name = input("Name: ")
    bid = input("Bid: ")
    people[name] = bid
    #print(people)
    answer = input("Are there more people? Answer yes or no: ")
    if answer == "yes":
        continue
    else:
        break