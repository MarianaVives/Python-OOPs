import time
from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake_obj = Snake()
food = Food()
score = Scoreboard()
is_race_on = True

screen.listen()

screen.onkey(key="Right", fun=snake_obj.move_right)
screen.onkey(key="Left", fun=snake_obj.move_left)
screen.onkey(key="Up", fun=snake_obj.move_up)
screen.onkey(key="Down", fun=snake_obj.move_down)

while is_race_on:
    screen.update()
    time.sleep(0.1)
    snake_obj.move_snake()

    #Detect collision with food
    if snake_obj.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake_obj.extend()

    #Detect collision with tail
    for seg in snake_obj.segments[1:]:
        if snake_obj.head.distance(seg) < 10:
            score.reset()
            snake_obj.reset()

    if snake_obj.head.xcor() > 290 or snake_obj.head.xcor() < -290 or snake_obj.head.ycor() > 290 or snake_obj.head.ycor() < -290:
        score.reset()
        snake_obj.reset()

screen.exitonclick()