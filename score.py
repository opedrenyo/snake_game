ALIGNMENT = "center"
FONT = ('Arial', 12, "normal")

from turtle import Turtle

class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.up()
        self.color("white")
        self.goto(x = 0, y = 360)
        self.update()
    
    def increase(self):
        self.score += 1
        self.update()

    def update(self):
        self.clear()
        self.write(arg =f"Score: {self.score}                 High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("high_score.txt", "w") as file:
            file.write(f"{self.high_score}")
        self.score = 0
        self.update()