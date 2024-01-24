'''
This is a game where user tries to name the states of the United States
Player can exit the game by typing exit
Game ends after all 50 states have been found
At the end the game will generate the states that were missing for player to learn
'''


import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

data = pd.read_csv("50_states.csv")
states = data.state.to_list()

score = 0
guessed_states = []

while score < 50:
    guess_box = str(screen.textinput(title=f"{score}/50 Guess the State", prompt="Name")).title()

    if guess_box == "Exit":
        missing_states = []
        for state in states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv", index=False)
        break

    if guess_box in states and guess_box not in guessed_states:
        guessed_states.append(guess_box)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == guess_box]
        t.goto(int(state_data.x), int(state_data.y)) # type: ignore
        t.write(guess_box)
        score += 1

