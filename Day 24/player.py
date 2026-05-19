from turtle import Turtle

STARTING_POSITION = (0, -200)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 200
UP = 90
DOWN = 270

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.move_to_start()
        self.setheading(UP)

    def move_player(self):
        self.forward(MOVE_DISTANCE)

    def move_up(self):
        self.setheading(UP)
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.setheading(DOWN)
        self.forward(MOVE_DISTANCE)

    def finish_game_win(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False

    def move_to_start(self):
        self.goto(STARTING_POSITION)