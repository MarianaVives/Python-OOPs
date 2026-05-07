import turtle
from turtle import Turtle, Screen
import random
import turtle as t

tim = Turtle()
t.colormode(255)

def generate_random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    my_color = (red, green, blue)
    return my_color


def draw_spirograph(size_gap):
    """Draw a spirograph"""
    tim.speed("fastest")
    for _ in range(int(360/size_gap)):
        tim.color(generate_random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_gap)

draw_spirograph(5)
screen = Screen()
screen.exitonclick()