import time
from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake_obj = Snake()
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



screen.exitonclick()





screen.exitonclick()