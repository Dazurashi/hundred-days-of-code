alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] #len = 26

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    coded_message = ""
    for letter in plain_text:
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

#TODO Math here is wonky
def decrypt(plain_text, shift_amount):
    coded_message = ""
    for letter in plain_text:
        pos = alphabet.index(letter)
        new_pos = pos - shift_amount 
        print(f"New pos is {new_pos, len(alphabet)}")
        if new_pos < len(alphabet) - 1:
            new_pos = abs(new_pos)
            print(f"New pos after if is {new_pos}")
            coded_message += alphabet[new_pos]
        else:
            coded_message += alphabet[new_pos]
    print(f"Decrypted message: {coded_message}")

# if direction == "encode":
#     encrypt(text, shift)
# elif direction == "decode":
#     decrypt(text, shift)
# else:
#     print("You didn't choose direction")

decrypt("byffi", 20) # Suppose to print "hello" but prints "teppm"