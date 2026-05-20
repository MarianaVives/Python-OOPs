from turtle import Turtle
UP = 90
DOWN = 270
STEPS = 10

class Paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(4, 1)
        self.penup()
        self.goto(x,y)

    def move_up(self):
        new_y = self.ycor() + STEPS
        self.goto(self.xcor(),new_y)

    def move_down(self):
        new_y = self.ycor() - STEPS
        self.goto(self.xcor(), new_y)
