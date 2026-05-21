import pandas as pd
import csv
import os
import turtle


file_path = os.path.join("utils_usagame","blank_states_img.gif")
current_dir = os.getcwd()
img_full_path = os.path.join(current_dir, file_path)

screen=turtle.Screen()
screen.title("Guess the USA State Name")

img =img_full_path
screen.addshape(img)

turtle.shape(img)

screen.exitonclick()