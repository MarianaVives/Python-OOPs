from turtle import Turtle
import random

colors_list = ["pink", "purple", "blue", "green", "lightblue", "red", "orange", "magenta", "yellow"]

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize( 0.5, 0.5)
        self.color(random.choice(colors_list))
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.color(random.choice(colors_list))
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        print("create new food in a random location")
