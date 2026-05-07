from turtle import Turtle, Screen
import random
import turtle as t

tim = Turtle()
colors = ["darkorchid", "hotpink", "deepskyblue", "wheat","seagreen"]
speed = ["fastest", "slow", "normal"]
directions = [0, 90, 100, 270]

t.colormode(255)

def generate_random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    my_color = (red, green, blue)
    return my_color


for _ in range(200):
    tim.forward(30)
    tim.width(15)
    tim.color(generate_random_color())
    tim.speed(random.choice(speed))
    tim.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()