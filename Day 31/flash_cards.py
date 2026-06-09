from tkinter import *
import pandas as pd
import os
import random

file_path = os.path.join("utils", "vocabulary_es_en.csv")
wrong_img_path = os.path.join("utils","wrong.png")
right_img_path = os.path.join("utils","right.png")
card_back_img_path = os.path.join("utils","card_back.png")
card_front_img_path = os.path.join("utils","card_front.png")
current_dir = os.getcwd()
csv_full_path = os.path.join(current_dir, file_path)
wrong_img= os.path.join(current_dir, wrong_img_path)
right_img = os.path.join(current_dir, right_img_path)
card_back_path= os.path.join(current_dir, card_back_img_path)
card_front_path = os.path.join(current_dir, card_front_img_path)

GREEN = "#9bdeac"
FONT_NAME = "Times New Roman"
SECONDS= 3000
#--- Read file ---
current_card={}
to_learn={}

try:
    #Read from the data frame of the words to study
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    #When running for the first time the file to read will be the original 100 words
    original_data = pd.read_csv(csv_full_path)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# --- Next Card ---
def next_card():
    global current_card, flip_timer
    wnd.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(lang_txt, text="Spanish", fill="black")
    canvas.itemconfig(word_txt, text=current_card["espanol"], fill="black")
    canvas.itemconfig(card_background, image=front_card)
    flip_timer = wnd.after(SECONDS, func=flip_cards)

#--- Flip Cards ---
def flip_cards():
    #After 3 seconds the card should flip over
    canvas.itemconfig(lang_txt, text="English", fill="white")
    canvas.itemconfig(word_txt, text=current_card["english"], fill="white")
    canvas.itemconfig(card_background,image=back_card)

# --- Cards guessed correctly ---
def is_known():
    to_learn.remove(current_card)
    # Save words to learn in a df
    data_learn = pd.DataFrame(to_learn)
    data_learn.to_csv("data/words_to_learn.csv", index=False)#index false does not include index in the df
    next_card()

# --- UI Settings ---
wnd = Tk()
wnd.title("Flash Cards")
wnd.configure(padx=20, pady=20, background=GREEN)
flip_timer = wnd.after(SECONDS, func=flip_cards)

canvas = Canvas(width=800, height=580, background=GREEN)
canvas.config(highlightthickness=0)
front_card=PhotoImage(file=card_front_path)
back_card=PhotoImage(file=card_back_path)
card_background = canvas.create_image(400,305, image=front_card)

lang_txt=canvas.create_text(390,180, text="Spanish", font=(FONT_NAME, 30, "italic"))
word_txt =canvas.create_text(390, 300, text = "", font=(FONT_NAME, 40, "bold"))
canvas.grid(row=0,column=0, columnspan=2)

# --- Buttons ---
wrong_image = PhotoImage(file=wrong_img)
button_wrong = Button(image=wrong_image, highlightthickness=0, command=is_known)
button_wrong.grid(row=1, column=0)

right_image = PhotoImage(file=right_img)
button_right = Button(image=right_image, highlightthickness=0, command=next_card)
button_right.grid(row=1, column=1)

next_card()

wnd.mainloop()