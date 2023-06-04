import random

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

allThree = [rock, paper, scissors]

computerChoice = random.choice(allThree)
playerChoice = allThree[int(input("Choose 1 for rock, 2 for paper or 3 for scissors: ")) - 1]
print(f"Computer chose {computerChoice}")
print(f"Player chose {playerChoice}")

if playerChoice == computerChoice:
    print("It'a draw...")
elif (playerChoice == rock and computerChoice == scissors) or (playerChoice == scissors and computerChoice == rock):
    print("Rock wins!")
elif (playerChoice == rock and computerChoice == paper) or (playerChoice == paper and computerChoice == rock):
    print("Paper wins!")
elif (playerChoice == scissors and computerChoice == paper) or (playerChoice == paper and computerChoice == scissors):
    print("Scissors win!")
else:
    print("You didn't choose anything")