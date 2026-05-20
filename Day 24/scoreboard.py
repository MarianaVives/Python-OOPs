from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Century Gothic',20,'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0,260)
        self.high_score = 0
        self.update_score()
        self.hideturtle()


    def update_score(self):
        self.clear_score()
        self.write(f"Score: {self.score} High Score: {self.high_score}",align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def clear_score(self):
        self.clear()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()
