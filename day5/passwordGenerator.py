'''
Asks user the amount of letters, symbols and numbers they want in their password.
Then generates a random password.
'''

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = []

num_letters = int(input("How many letters? :"))
num_numbers = int(input("How many numbers? :"))
num_symbols = int(input("How many symbols? :"))

for letter in range(0, num_letters):
    password.insert(random.randint(0, len(password)), letters[random.randint(0, len(letters) - 1)])

for number in range(0, num_numbers):
    password.insert(random.randint(0, len(password)), numbers[random.randint(0, len(numbers) - 1)])

for symbol in range(0, num_symbols):
    password.insert(random.randint(0, len(password)), symbols[random.randint(0, len(symbols) - 1)])

password = "".join(password)

print(f"Here is your new password: {password}")