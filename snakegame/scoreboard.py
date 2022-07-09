from re import A
from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 15, 'normal')
with open("data.txt", "r") as data:
    hs = int(data.read())

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.up()
        self.goto(0, 270)
        self.shapesize(0.1,0.1)
        self.speed("fastest")
        self.hideturtle()
        self.score = -1
        self.high_score = hs
        self.update_scoreboard()

    def update_scoreboard(self):
        self.increase_score()
        self.write(f"Score: {self.score} High Score: {self.high_score}" , align=ALIGNMENT, move=False, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = -1
        self.update_scoreboard()
        with open("high_score.txt", mode="w") as file:
            file.write(f"{self.high_score}")

    def increase_score(self):
        self.clear()
        self.score +=1

