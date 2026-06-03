import pandas as pd
import csv
import os
import turtle


img_file_path = os.path.join("utils_usagame", "blank_states_img.gif")
csv_file_path = os.path.join("utils_usagame", "50_states.csv")
current_dir = os.getcwd()
img_full_path = os.path.join(current_dir, img_file_path)
states_full_path = os.path.join(current_dir, csv_file_path)

screen = turtle.Screen()
t = turtle.Turtle()
screen.title("Guess the USA State Name")

img =img_full_path
screen.addshape(img)

guessed_states=[]
score = 0

data = pd.read_csv(csv_file_path)
state_list = data.state.to_list()

def ask_user_for_another_state():
    answer_state = screen.textinput(f"Guess the State: {len(guessed_states)}/50", prompt="What is another state's name? ").title()
    return answer_state

def move_turtle(answer):
    guessed_states.append(answer)
    t.hideturtle()
    t.penup()
    state_data = data[data.state == answer]
    t.goto(float(state_data.x.item()), float(state_data.y.item()))
    t.write(ans)


while len(guessed_states) < 50:
    turtle.shape(img)
    ans = ask_user_for_another_state()
    if ans == "Exit":
        missing_states=[s for s in state_list if s not in guessed_states]
        #missing_states = []
        #for state in state_list:
        #    if state not in guessed_states:
        #        missing_states.append(state)
        missing_states_df = pd.DataFrame(missing_states)
        missing_states_df.to_csv("states_to_study.csv")

        break
    if ans in state_list:
        move_turtle(ans)




screen.exitonclick()