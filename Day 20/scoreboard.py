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

        self.update_score()
        self.hideturtle()


    def update_score(self):
        self.write(f"Score: {self.score}",align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear_score()
        self.update_score()

    def clear_score(self):
        self.clear()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over",align=ALIGNMENT,font=FONT)