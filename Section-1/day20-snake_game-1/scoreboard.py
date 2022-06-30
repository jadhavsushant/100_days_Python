from turtle import Turtle
# scoreboard contract
SCORE_LOCATION = (0, 260)
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.penup()
        self.color("white")
        self.goto(SCORE_LOCATION)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score : {self.current_score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.current_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!!!", font=FONT, align="center")



