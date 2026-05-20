import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "magenta"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LEFT = 180

class CarManager():
    def __init__(self):
        super().__init__()
        self.cars=[]
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = random.randint(0, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1,2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.setheading(LEFT)
            new_car.goto(190 ,random.randint(-180, 200))
            self.cars.append(new_car)

    def move_cars(self):
        for c in self.cars:
            c.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT