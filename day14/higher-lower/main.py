'''
    The program will give user two people and basic onfo about them.
    User tries to guess which of them have bugger social media following.
    Game ends when user guesses wrong.
'''

from art import logo, vs
from data import data
import random
from os import system

people_list = data
score = -1
game_over = False

def randomizePerson():
    return random.choice(people_list)

def compareFollowers(first, second):
    if first['follower_count'] > second['follower_count']:
        return 1
    else:
        return 0
    
def checkGameStatus(state):
    if state == 0:
        print("Game Over")
        return True

personA = randomizePerson()

while game_over != True:
    score += 1
    system("clear")
    print(logo)
    print(f"Your current score is: {score}")
    print(f"Compare A: {personA['name']}, {personA['description']} from {personA['country']}.")
    print(vs)
    personB = randomizePerson()
    print(f"Against B: {personB['name']}, {personB['description']} from {personB['country']}")

    answer = input("Who has more social media followers? Type A or B: ").lower()
    if answer == "a":
        answer = int(compareFollowers(personA, personB))
    elif answer == "b":
        answer = int(compareFollowers(personB, personA))
    game_over = checkGameStatus(answer)
    people_list.remove(personA)
    personA = personB
    