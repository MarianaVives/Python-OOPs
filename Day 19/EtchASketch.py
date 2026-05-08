from turtle import Turtle, Screen

tom = Turtle()
screen = Screen()

def move_forwards():
    tom.forward(10)

def move_backwards():
    tom.backward(10)

def move_anticlockwise():
    tom.left(10)
    tom.forward(10)

def move_clockwise():
    tom.right(10)
    tom.forward(10)

def clear():
    tom.clear()
    tom.penup()
    tom.home()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_anticlockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()