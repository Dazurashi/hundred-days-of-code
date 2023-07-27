import turtle as t

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.starting_pos()
        self.left(90)

    def move (self):
        y_cord = self.ycor() + MOVE_DISTANCE
        self.goto(0, y_cord)

    def is_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
        
    def starting_pos(self):
        self.goto(STARTING_POSITION)

    