import turtle as t
import time

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('orange')
screen.title("Snake Game")
screen.tracer(0)
game_running = True

segments = []

starting_pos = [(0, 0), (-20, 0), (-40, 0)]
for pos in starting_pos:
    block = t.Turtle('square')
    block.penup()
    block.goto(pos)
    segments.append(block)

while True:
    screen.update()
    time.sleep(0.1)
    for i in segments:
        i.forward(20)
        




screen.exitonclick()