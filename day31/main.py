'''
This is a simple flash card application demo.
User has 3 seconds to call out the word or meaning before the answer is revealed.
Clicking red button will return the word into the stack and green button removes it.
Progress is saved after the app is closed.
'''

import tkinter as tk
import pandas as pd
import random

#-------------CONSTANTS-------------------#
BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pd.read_csv("data/still_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")

new_words = data.to_dict(orient="records")
current_card = {}


#------------MECHANICS-------------------#
def known():
    '''Triggered when green green button is pressed. Deletes the known word.'''
    global current_card
    new_words.remove(current_card)
    new_data = pd.DataFrame(new_words)
    new_data.to_csv("data/still_to_learn.csv", index=False)
    next()

def flip():
    '''Flips the card.'''
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card, image=card_back_img)

def next():
    '''Switches to next card.'''
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(card, image=card_front_img)
    current_card = random.choice(new_words)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, flip)
    


#-------------GUI------------------------#
window = tk.Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip)

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=False)
card_front_img = tk.PhotoImage(file="images/card_front.png")
card_back_img = tk.PhotoImage(file="images/card_back.png")
card = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

red_img = tk.PhotoImage(file="images/wrong.png")
red_button = tk.Button(image=red_img, borderwidth=0, highlightthickness=False, command=next)
red_button.grid(row=1, column=0)

green_img = tk.PhotoImage(file="images/right.png")
green_button = tk.Button(image=green_img, borderwidth=0, highlightthickness=False, command=known)
green_button.grid(row=1, column=1)

next()

window.mainloop()