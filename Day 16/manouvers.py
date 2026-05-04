from turtle import Turtle, Screen

tortu = Turtle()
tortu.color("blue")
tortu.shape("turtle")

def move_in_square():
    tortu.forward(100)
    tortu.left(90)
    tortu.forward(100)
    tortu.left(90)
    tortu.forward(100)
    tortu.left(90)
    tortu.forward(100)

def move_in_hexagon():
    tortu.forward(100)
    tortu.right(45)
    tortu.forward(100)
    tortu.right(45)
    tortu.forward(100)
    tortu.right(45)
    tortu.forward(100)
    tortu.right(45)
    tortu.forward(100)
    tortu.right(45)
    tortu.forward(100)
    tortu.right(45)
    tortu.forward(100)
    tortu.right(45)
    tortu.forward(100)
    tortu.right(45)

def move_in_triangle():
    tortu.forward(200)
    tortu.left(120)
    tortu.forward(100)
    tortu.left(120)
    tortu.forward(100)
    tortu.left(120)