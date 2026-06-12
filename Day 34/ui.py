import os
from tkinter import *
from quiz_app import QuizBrain

#--- Colors ---
BABY_BLUE_SPACE = "#EFF6E0"
DEEP_SPACE_BLUE = "#01161E"
SOFT_PERIWINKLE = "#AEC3B0"
FONT = "Arial"
# --- images ---
wrong_img_path = os.path.join("utils", "wrong.png")
right_img_path = os.path.join("utils", "right.png")
current_dir = os.getcwd()
wrong_img = os.path.join(current_dir, wrong_img_path)
right_img = os.path.join(current_dir, right_img_path)


class QuizInterface():
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz_brain = quiz_brain
        #initialize attributes
        #--- UI CONFIG ---
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=SOFT_PERIWINKLE)
        # --- LABEL ---
        self.score_label = Label(self.window, text="Score: 0", fg="black", font=(FONT, 10), bg=SOFT_PERIWINKLE)
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(self.window, width=300, height=250, highlightthickness=0, bg=BABY_BLUE_SPACE)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # --- BUTTONS ---
        self.button_true = Button(background=SOFT_PERIWINKLE)
        self.button_false = Button(background=SOFT_PERIWINKLE)
        wrong_image = PhotoImage(file=wrong_img)
        self.button_wrong = Button(image=wrong_image, highlightthickness=0,  command= self.false_answer)
        self.button_false.config(bg=SOFT_PERIWINKLE)
        self.button_wrong.grid(row=2, column=0)
        right_image = PhotoImage(file=right_img)
        self.button_right = Button(image=right_image, highlightthickness=0, command= self.true_answer)
        self.button_right.grid(row=2, column=1)
        # --- TEXT ---
        self.my_question = self.canvas.create_text(150, 125, text="MY QUESTION GOES HERE ...",
                                                   width=280, font=(FONT, 16, "italic"), fill=DEEP_SPACE_BLUE)
        self.get_next_question()
        self.window.mainloop()

    def false_answer(self):
        is_right = self.quiz_brain.is_answer_correct("False")
        self.give_feedback(is_right)

    def true_answer(self):
        is_right = self.quiz_brain.is_answer_correct("True")
        self.give_feedback(is_right)

    def give_feedback(self, answer: bool):
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    def get_next_question(self):
        if self.quiz_brain.still_has_questions():
            self.canvas.config(bg= BABY_BLUE_SPACE)
            self.score_label.config(text=f"Score: {self.quiz_brain.score}")
            question_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.my_question, text=question_text)
        else:
            self.canvas.config(bg=BABY_BLUE_SPACE)
            self.canvas.itemconfig(self.my_question, text=f"You have answered all questions. \nYour score is {self.quiz_brain.score}/10")
            self.button_wrong.config(state="disabled")
            self.button_right.config(state="disabled")