ALIGNMENT = "center"
FONT = ('Arial', 12, "normal")

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
    
    def increase(self):
        self.score += 1
        self.clear()
        self.update_score()

    def update(self):
        self.write(arg =f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(x = 0, y = 0)
        self.write(arg="Game Over.", align = ALIGNMENT, font = FONT)