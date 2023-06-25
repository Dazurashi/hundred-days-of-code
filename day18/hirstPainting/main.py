'''
    This program draws a similar hist painting that were sold for fortune.
'''

import turtle as t
import random

dots = 100

t.colormode(255)
tutel = t.Turtle()
tutel.speed('fastest')
tutel.hideturtle()
tutel.penup()
tutel.setheading(225)
tutel.forward(300)
tutel.setheading(0)

for i in range(1, dots + 1):
    tutel.dot(20, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    tutel.forward(50)
    if i % 10 == 0:
        tutel.setheading(90)
        tutel.forward(50)
        tutel.setheading(180)
        tutel.forward(500)
        tutel.setheading(0)

screen = t.Screen()
screen.exitonclick()