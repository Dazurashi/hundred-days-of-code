import turtle as t

ALIGN = "center"
FONT = ("Arial", 20, "normal")

class ScoreBoard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_score()

    def scored(self):
        self.score += 1
        self.clear()
        self.update_score()
        
    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)
        