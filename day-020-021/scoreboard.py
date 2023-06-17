from turtle import Turtle
_ALIGNMENT = "center"
_FONT = ("Arial", 24, "normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=_ALIGNMENT, font=_FONT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()