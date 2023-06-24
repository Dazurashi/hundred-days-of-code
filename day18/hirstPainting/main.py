import turtle as t
import random

t.colormode(255)
tutel = t.Turtle()


tutel.dot(20, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

screen = t.Screen()
screen.exitonclick()