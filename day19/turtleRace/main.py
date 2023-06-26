'''
    In this program there are 5 turtles.
    User is asked to bet on a color.
    Once race is finished, the winner is announced.
'''

import turtle as t
import random

race = False
screen = t.Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Bet", prompt="Bet a color to win the race.\nYour options are: red, blue, purple, yellow, green and orange")
ypos = -100
colors = ["red", "blue", "purple", "yellow", "green", "orange"]
race_tutels = []

for i in range(0, 6):
    tutel = t.Turtle(shape='turtle')
    tutel.color(colors[i])
    race_tutels.append(tutel)
    tutel.penup()
    tutel.goto(x=-230, y=ypos)
    ypos += 40
if bet:
    race = True

while race:
    movement = random.randint(0, 10)
    chosen_tutel = random.choice(race_tutels)
    chosen_tutel.forward(movement)
    if chosen_tutel.xcor() > 230:
        print(f"{chosen_tutel.pencolor().title()} wins the race!\nYour bet was: {bet}")
        break
    
    



screen.exitonclick()