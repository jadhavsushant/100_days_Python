from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_player = 0
        self.r_player = 0
        self.scoreboard()

    def scoreboard(self):
        self.goto(-100, 250)
        self.write(self.l_player, align="center", font=("courier", 30, "normal"))
        self.goto(100, 250)
        self.write(self.r_player, align="center", font=("courier", 30, "normal"))

    def l_score(self):
        self.l_player += 1
        self.scoreboard()

    def r_score(self):
        self.r_player += 1
        self.scoreboard()