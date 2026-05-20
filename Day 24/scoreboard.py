from turtle import Turtle
import os
file_path = os.path.join("utils","data_file.txt")
current_dir = os.getcwd()
full_path = os.path.join(current_dir, file_path)

ALIGNMENT = "center"
FONT = ('Century Gothic',20,'normal')
FILE_PATH= full_path
with open(FILE_PATH, mode="r") as file:
    score_data = file.read()

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0,260)
        self.high_score = int(score_data)
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
            with open(FILE_PATH, "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()
