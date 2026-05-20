from turtle import Turtle

class PongScreen:
    def __init__(self):
        super().__init__()
        self.turtle = Turtle()

    def create_wall(self):
        self.turtle.hideturtle()
        self.turtle.color("white")
        self.turtle.speed("fastest")
        self.turtle.penup()
        self.turtle.goto(0,-250)
        self.turtle.setheading(90)
        for _ in range(50):
            self.turtle.pendown()
            self.turtle.forward(5)
            self.turtle.penup()
            self.turtle.forward(5)
