'''
    User tries to guess a random number between 1 and 100.
    They can also choose hard or normal difficulty. 
    Hard gives you 5 tries and normal 10.
    After every guess the program tells you if the number is higher or lower than user guessed.
'''
import random
from art import logo
print(logo)

hidden_number = random.randint(1, 100)
game_over = False

def difficultyLevel(diff):
    if diff == "hard":
        return 5
    elif diff == "normal":
        return 10
    else: 
        return 0
    

def checkGuess(num):
    if num > hidden_number:
        print("Lower")
    elif num < hidden_number:
        print("Higher")
    else:
        return 0

lives = difficultyLevel(input("Choose 'normal' or 'hard' difficulty: ").lower())

while not game_over:
    if lives == 0:
        print(f"Game Over!\nThe number was {hidden_number}")
        game_over = True
    else:
        print(f"You have {lives} lives left")
        guess = int(input("Guess the number: "))
        if checkGuess(guess) == 0:
            print("You guessed right!")
            game_over = True
        lives -= 1