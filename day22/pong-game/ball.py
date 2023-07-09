import turtle as t

class Ball(t.Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce(self):
        self.y_move *= -1

    def catch(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0,0)
        self.catch()