import turtle as t
#TODO movement with keyboard
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.make_snake()

    def make_snake(self):
        for pos in STARTING_POS:
            block = t.Turtle('square')
            block.penup()
            block.goto(pos)
            self.segments.append(block)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            xpos = self.segments[i - 1].xcor()
            ypos = self.segments[i - 1].ycor()
            self.segments[i].goto(xpos, ypos)
        self.segments[0].forward(MOVE_DISTANCE)