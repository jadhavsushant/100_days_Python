from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.score = 0
        self.penup()
        self.hideturtle()
        self.score_board()

    def score_board(self):
        self.clear()
        self.goto(-250, 250)
        self.write(f" Score={self.score}", align="left", font=FONT)

    def update_score(self):
        self.score += 1
        self.score_board()



