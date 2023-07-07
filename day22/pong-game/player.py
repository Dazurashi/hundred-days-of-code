import turtle as t

class Player(t.Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(pos)
        

    def go_up(self):
        y_cord = self.ycor() + 20
        self.goto(self.xcor(), y_cord)

    def go_down(self):
        y_cord = self.ycor() - 20
        self.goto(self.xcor(), y_cord)