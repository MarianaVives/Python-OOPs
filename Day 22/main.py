import time
from turtle import Turtle, Screen
from pongscreen import PongScreen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball

PLAYER_A_NAME= "A"
PLAYER_B_NAME= "B"

class Pong(Turtle):
    def __init__(self):
        super().__init__()

    screen = Screen()
    screen.title("Pong")
    screen.listen()
    screen.bgcolor("black")
    scoreboard_a = Scoreboard(-200,290, PLAYER_A_NAME)
    scoreboard_b = Scoreboard(200, 290, PLAYER_B_NAME)
    pong_screen = PongScreen()
    pong_screen.create_wall()

    paddle_b = Paddle(350,0)
    paddle_a = Paddle(-350,0)

    screen.setup(width=800,height=700)

    screen.onkey(fun=paddle_b.move_up,key="Up")
    screen.onkey(fun=paddle_b.move_down,key="Down")
    screen.onkey(fun=paddle_a.move_up,key="w")
    screen.onkey(fun=paddle_a.move_down,key="s")
    ball = Ball()

    game_on = True

    while game_on:
        ball.move_forward()
        screen.update()
        time.sleep(0.1)
        if ball.ycor() > 280 or ball.ycor() <- 280:
            ball.bounce_y()
        #collision with right paddle
        if paddle_b.distance(ball) < 50 and ball.xcor()<349:
            ball.bounce_x()
            scoreboard_b.increase_score()
        elif paddle_a.distance(ball) < 50 and ball.xcor()<349:
            ball.bounce_x()
            scoreboard_a.increase_score()

        if ball.collision_with_wall():
            ball.game_over()
            time.sleep(.3)
            ball.write_winner(scoreboard_a.score,scoreboard_b.score, PLAYER_A_NAME, PLAYER_B_NAME)
            game_on = False


    screen.exitonclick()