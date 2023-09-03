import turtle as t

ALIGN = "center"
FONT = ("Arial", 20, "normal")
HS_FILE = open("highscore.txt", mode="r")

class ScoreBoard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = HS_FILE.read()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_score()

    def scored(self):
        self.score += 1
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGN, font=FONT)

    def reset(self):
        if int(self.highscore) < self.score:
            with open("highscore.txt", mode="w") as f:
                f.write(str(self.score))
        self.score = 0

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGN, font=FONT)
        