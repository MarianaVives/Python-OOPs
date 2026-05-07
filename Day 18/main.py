from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("hotpink")

colors = ["darkorchid", "hotpink", "deepskyblue", "wheat","seagreen"]
def get_angle(num_sides):
    return  360 / num_sides

def move_in_square():
    """Turtle moves in square"""
    for _ in range(4):
        for _ in range(2):
            timmy_the_turtle.forward(25)
            timmy_the_turtle.color("white")
            timmy_the_turtle.forward(25)
            timmy_the_turtle.color("hotpink")
        timmy_the_turtle.left(get_angle(4))

def move_in_triangle():
    """Turtle moves in triangle"""
    timmy_the_turtle.color(random.choice(colors))
    for _ in range(3):
        for _ in range(2):
            timmy_the_turtle.forward(10)
            timmy_the_turtle.penup()
            timmy_the_turtle.forward(15)
            timmy_the_turtle.pendown()
        timmy_the_turtle.left(get_angle(3))

def move_in_hexagon():
    """Turtle moves in hexagon"""
    for _ in range(6):
        timmy_the_turtle.forward(10)
        timmy_the_turtle.left(45)

def move_in_shape(s, num_sides):
    """Turtle moves in any shape defined by the number of sides."""
    for _ in range(num_sides):
        steps = s/num_sides
        timmy_the_turtle.color(random.choice(colors))
        timmy_the_turtle.forward(steps)
        timmy_the_turtle.left(get_angle(num_sides))



n=3
s = 100
for _ in range(10):
    move_in_shape(s, n)
    n+=1
    s+=100


screen = Screen()
screen.exitonclick()