import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreborard import Scoreboard

screen=Screen()
player = Player()
car = CarManager()
score = Scoreboard()

screen.title("Cross the road")
screen.setup(width=600, height=600)
screen.tracer(0)


is_game_on = True
screen.listen()
screen.onkey(key="Up", fun=player.move_up)
screen.onkey(key="Down", fun=player.move_down)
while is_game_on:
    time.sleep(0.1)
    screen.update()
    #Generate random cars and Move
    car.create_cars()
    car.move_cars()
    for c in car.cars:
        if c.distance(player) < 30:
            is_game_on = False
    #Detect when player reaches finish line
    if player.finish_game_win():
        player.move_to_start()
        score.increase_score()
        car.level_up()


screen.exitonclick()