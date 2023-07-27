import turtle as t

FONT = ("Courier", 24, "normal")


class Scoreboard(t.Turtle):
    def __init__(self):
        self.level = 1
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_level()
        

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def level_up(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align="center", font=FONT)
        

