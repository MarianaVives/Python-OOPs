#import turtle
from turtle import Turtle, Screen
import manouvers

tortu = Turtle()
my_screen = Screen()
print(my_screen.canvheight)

manouvers.move_in_square()
manouvers.move_in_hexagon()
manouvers.move_in_triangle()
manouvers.move_in_triangle()
my_screen.exitonclick() # Screenshowup and disappear

