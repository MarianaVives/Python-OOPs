from turtle import Turtle
import random

colors = ["red","orange","yellow","green","blue","violet","magenta","pink","skyblue"]
STEPS_BALL = 10
SPEED_INCREMENT = 0.9
angle_random = random.randint(-20, 20)
LEFT = 180
RIGHT = 0
FONT = ("Arial",20,"bold")
FONT_GAMEOVER = ("Arial",40,"bold")


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color(random.choice(colors))
        self.penup()
        self.x_move=10
        self.y_move=10
        self.speed_ball = 0.1

    def move_forward(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *=-1

    def bounce_x(self):
        self.color(random.choice(colors))
        self.x_move *= -1
        self.speed_ball *= SPEED_INCREMENT


    def collision_with_wall(self):
        if  self.xcor() > 380 or self.xcor() < -380:
            return True
        else:
            return False

    def game_over(self):
        self.hideturtle()
        self.color("blue")
        self.goto(0,50)
        self.write("Game Over",align="center",font=FONT_GAMEOVER)

    def write_winner(self, score_a, score_b, name_a, name_b):
        self.hideturtle()
        self.color("yellow")
        self.goto(0,0)
        if score_a > score_b:
            self.write(f"The winner is player {name_a} with a Score of:  {score_a}",align="center",font=FONT)
        elif score_b > score_a:
            self.write(f"The winner is player {name_b} with a Score of:  {score_b}",align="center",font=FONT)
        else:
            self.write("Its a Draw",align="center",font=FONT)