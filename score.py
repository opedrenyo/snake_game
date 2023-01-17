ALIGNMENT = "center"
FONT = ('Calibri', 14, "bold")

from turtle import Turtle

class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.up()
        self.color("white")
        self.goto(x = 0, y = 360)
        self.update_score()
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def update_score(self):
        self.write(arg =f"Score: {self.score}", align=ALIGNMENT, font=FONT)
