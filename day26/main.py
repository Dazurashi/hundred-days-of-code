'''
This program will take a word as an input from the user and transfer it into list of NATO alphabets
ex: input = "Bob" -> output = ['Bravo', 'Oscar', 'Bravo']
'''

import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
nato_letters = {row.letter:row.code for (index, row) in data.iterrows()}

def generate():
    try:
        nato_list = [nato_letters[letter] for letter in input("Enter a word: ").upper()]
    except KeyError:
        print("Use letters only!")
        generate()
    else:
        print(nato_list)
generate()