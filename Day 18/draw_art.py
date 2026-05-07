import random
from turtle import Turtle, Screen
import turtle
#install pip install colorgram.py
import colorgram

t = Turtle()
turtle.colormode(255)
color_palette = [(237, 236, 233), (233, 241, 236), (166, 151, 135), (232, 233, 241), (242, 233, 241), (222, 206, 123), (143, 101, 88), (120, 88, 99), (83, 89, 127), (196, 96, 83), (149, 163, 185), (156, 145, 154), (103, 38, 46), (137, 154, 140), (132, 123, 132), (47, 45, 94), (41, 24, 42), (144, 146, 90), (112, 127, 101), (175, 34, 20), (118, 126, 154), (215, 179, 176), (66, 71, 55), (123, 140, 107), (0, 0, 0)]
t.hideturtle()

def extract_colors():
    """Extract 30 colors from an image."""
    colors = colorgram.extract('damien hirst spots.png', 30)
    color_list = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        color_item = (r, g, b)
        color_list.append(color_item)
    print(color_list)

def dotted_pattern():
    t.dot(20, random.choice(color_palette))
    t.forward(40)

def create_art():
    """Generate arte Damien Hirst style"""
    rows = 0
    x,y = -250,-300
    t.penup()
    while rows <=12:
        for c in (color_palette):
            t.goto(x,y)
            for _ in range(12):
                dotted_pattern()
                y += 5
            t.goto(x, y)
            rows += 1


create_art()
screen = Screen()
screen.screensize(1200, 1200)

screen.exitonclick()