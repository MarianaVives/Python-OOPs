import time
from turtle import Turtle, Screen

STARTING_POSITIONS=[(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
LEFT = 180
RIGHT = 0
UP = 90
DOWN = 270

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.move_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            square = Turtle(shape="square")
            square.color("white")
            square.penup()
            square.goto(position)
            self.segments.append(square)

    def move_snake(self):

        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x= self.segments[seg_num -1].xcor()
            new_y= self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
            if self.segments[seg_num].xcor() > 560 or self.segments[seg_num].ycor() > 560:
                return False
                print("Lost")
        self.segments[0].forward(MOVE_DISTANCE)

    def move_up(self):
        print("Moving up")
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        print("Moving down")
        if self.head.heading() != RIGHT:
            self.head.setheading(DOWN)

    def move_left(self):
        print("Moving left")
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        print("Moving right")
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

