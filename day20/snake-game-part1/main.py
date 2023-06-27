import turtle as t

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('orange')
screen.title("Snake Game")

starting_pos = [(0, 0), (-20, 0), (-40, 0)]
for pos in starting_pos:
    block = t.Turtle('square')
    block.goto(pos)

screen.exitonclick()