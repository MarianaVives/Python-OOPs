import os
from tkinter import *
import math

file_path = os.path.join("util", "tomato.png")
current_dir = os.getcwd()
img_full_path = os.path.join(current_dir, file_path)
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_txt, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1

    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps == 8:
        title_label.config(text="Break", fg=PINK)
        count_down(long_break_sec)
    elif reps%2!=0:
        title_label.config(text="Work", fg=RED)
        count_down(work_sec)

    else:
        title_label.config(text="Break", fg=GREEN)
        count_down(short_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    minutes= math.floor(count/60)
    seconds= count%60
    #Make sure that if less than two digits, add a 0 at the begining
    if len(str(abs(seconds)))<2:
        seconds="0"+str(seconds)
    #Update the number in the timer to the new mins and secs
    canvas.itemconfig(timer_txt, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark=""
        work_sessions=math.floor(reps/2)
        for _ in range(work_sessions):
            mark+="✓"
            check_marks.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)


#Create Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img=PhotoImage(file=img_full_path)
canvas.create_image(100, 112, image=tomato_img)
timer_txt= canvas.create_text(100, 134, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)
title_label = Label(text="Timer", fg=PINK, font=(FONT_NAME, 30), bg=YELLOW)
title_label.grid(row=0, column=1)

#calls action() when pressed
btn_reset = Button(text="Reset", bg=PINK, highlightthickness=0, font=(FONT_NAME, 20), command=reset_timer)
btn_reset.grid(row=4, column=3)

#calls action() when pressed
btn_start = Button(text="Start",  bg=PINK, highlightthickness=0, font=(FONT_NAME, 20), command=start_timer)
btn_start.grid(row=4, column=0)

check_marks = Label(fg=GREEN,font=(FONT_NAME, 30, "bold"), bg=YELLOW)
check_marks.grid(row=4, column=1)

#5,3
window.mainloop()
