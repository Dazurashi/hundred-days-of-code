'''
This program will take a word as an imput from the user and transfor it into list of NATO alphabets
ex: input = "Bob" -> output = ['Bravo', 'Oscar', 'Bravo']
'''

import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
nato_letters = {row.letter:row.code for (index, row) in data.iterrows()}
nato_list = [nato_letters[letter] for letter in input("Enter a word: ").upper()]
print(nato_list)