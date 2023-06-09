'''
    Program asks user if they want to encode or decode a message.
    Encoding uses Caesar cipher so user is then asked to number of shifts in alphabets.
'''

from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] #len = 26

print(logo)

def caesar(plain_text, shift_amount, dir):
    coded_message = ""

    if dir == "decode":
        shift_amount *= -1

    for letter in plain_text:
        if letter not in alphabet:
            coded_message += letter
        else:
            pos = alphabet.index(letter)
            new_pos = pos + shift_amount
            #Perhaps more easier trick would've been adding letters twice into alphabets if new_pos goes out of range
            #But that's boring and I wanted to flex my algorithmic solution over petty tricks 
            if new_pos > len(alphabet) - 1:
                new_pos = new_pos - len(alphabet)
                coded_message += alphabet[new_pos]
            else:
                coded_message += alphabet[new_pos]

    print(f"Encrypted message: {coded_message}")

while(True):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    answer= input("Type 'y' if you want to continue using the program. Otherwise type 'n': ").lower()
    if answer == "y":
        continue
    elif answer == "n":
        break
    else: 
        print("I take that as a no")
        break