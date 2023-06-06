'''
    Hangman game. If you don't know it then I'm speechless.
'''

import random
import art
import words

print(art.logo)
word_list = words.word_list
#chosen_word = word_list[random.randint(0, len(word_list) - 1)] <---- This one was too lengthy so made it shorter below
chosen_word = random.choice(word_list)
lives = 6
#print(chosen_word)
empty_word = []


for i in range(len(chosen_word)):
    empty_word.append("_")

def checkLetter():
    for index, letter in enumerate(chosen_word):
        if letter == guess_letter:
            empty_word[index] = guess_letter
            
            
while True:
    if "".join(empty_word) == chosen_word:
        print("You win")
        break
    elif lives == -1:
        print(f"You are dead. The word was {chosen_word}")
        break
    else:
        print(f"You have {lives} lives left")
        guess_letter = input("Guess a letter: ").lower()
        if guess_letter not in chosen_word:
            print(art.stages[lives])
            lives -= 1
            print(empty_word)
            print()
        else:
            checkLetter()
            print(empty_word)
            print()