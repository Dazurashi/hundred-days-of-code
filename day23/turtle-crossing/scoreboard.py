import turtle as t

FONT = ("Courier", 24, "normal")


class Scoreboard(t.Turtle):
    def __init__(self):
        self.level = 1
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.write(f"Level: {self.level}", align="left", font=FONT)
