'''
Password manager that helps the user to remember their passwords and usernames
User is able to generate the password
Everything is stored in a text file data.txt
Before adding, user is asked for confirmation and an error is shown if any of the fields are empty
'''

import tkinter as tk
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [random.choice(letters) for _ in range(0, random.randint(8, 10))]
    number_list = [random.choice(numbers) for _ in range(0, random.randint(2, 4))]
    symbol_list = [random.choice(symbols) for _ in range(0, random.randint(2, 4))]

    password = letter_list + number_list + symbol_list
    random.shuffle(password)
    password = "".join(password)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    ws = website_entry.get()
    em = email_entry.get()
    pw = password_entry.get()

    if len(ws) == 0 or len(em) == 0 or len(pw) == 0:
        messagebox.showerror(title="Error", message="One or more fields are empty!")

    elif messagebox.askokcancel(title="Confirm", message=f"Would you like to save the following data?\nWebsite: {ws}\nEmail: {em}\nPassword: {pw}"):
        with open("data.txt", mode="a+") as file:
            file.write(f"{ws} | {em} | {pw}\n")
            
        website_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#Labels
website_label = tk.Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = tk.Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = tk.Label(text="Password:")
password_label.grid(column=0, row=3)

#Entries
website_entry = tk.Entry(width=52)
website_entry.grid(column=1, row=1, columnspan=2, sticky="W")
website_entry.focus()

email_entry = tk.Entry(width=52)
email_entry.grid(column=1, row=2, columnspan=2, sticky="W")

password_entry = tk.Entry(width=34)
password_entry.grid(column=1, row=3, sticky="W")

#Buttons
generate_button = tk.Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3, sticky="W")

add_button = tk.Button(text="Add", width=44, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="W")

window.mainloop()