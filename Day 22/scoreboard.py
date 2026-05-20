from turtle import Turtle

FONT = ("Arial",20,"bold")

class Scoreboard(Turtle):
    def __init__(self,x,y,name):
        super().__init__()
        self.name=name
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x,y)
        self.update_score()

    def clear_score(self):
        self.clear()

    def update_score(self):
        self.write(f"Player {self.name} : {self.score}",align="center",font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear_score()
        self.update_score()



