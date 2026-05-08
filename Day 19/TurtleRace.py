from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange",  "yellow", "green", "skyblue", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]
speed = ["fastest", "fast", "normal", "slow", "slowest"]
is_race_on = False

turtles_list = []
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
"""Create objects of the class turtle for the race and add them to a list of turtles in the race (size 6)"""
for t_index in range(0,6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[t_index])
    new_turtle.goto(x=0, y=y_pos[t_index])
    turtles_list.append(new_turtle)

if user_bet:
    is_race_on=True

while is_race_on:
    for t in turtles_list:
        if t.xcor() > 210:
            is_race_on = False
            winning_color = t.color()
            if winning_color == user_bet:
                print(f"Turtle with color: {winning_color} won. You win the bet!")
            else:
                print(f"Turtle with color: {winning_color} won. You lost the bet!")
        rand_distance= random.randint(0,10)
        t.forward(rand_distance)

screen.exitonclick()

