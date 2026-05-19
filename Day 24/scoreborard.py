from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(0,250)
        self.player_score = 0
        self.update_score()

    def increase_score(self):
        self.player_score += 1
        self.clear_score()
        self.update_score()

    def update_score(self):
        self.write(f"Score : {self.player_score}", align="center", font= FONT)

    def clear_score(self):
        self.clear()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font= FONT)