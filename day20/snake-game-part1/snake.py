import turtle as t
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.make_snake()
        self.head = self.segments[0]

    def make_snake(self):
        for pos in STARTING_POS:
            self.add_segment(pos)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self, pos):
        block = t.Turtle('square')
        block.penup()
        block.goto(pos)
        self.segments.append(block)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            xpos = self.segments[i - 1].xcor()
            ypos = self.segments[i - 1].ycor()
            self.segments[i].goto(xpos, ypos)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)