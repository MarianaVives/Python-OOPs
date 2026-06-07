import os
from tkinter import *
from tkinter import messagebox
import random
import pyperclip

file_path = os.path.join("utils", "logo.png")
current_dir = os.getcwd()
img_full_path = os.path.join(current_dir, file_path)

FONT_NAME = "Arial"
FONT_NAME_2 = "Courier"
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["1","2","3","4","5","6","7","8","9","0"]
symbols = ["#","$","%","&","*","@","!",".","+","-"]

num_letters = random.randint(8, 10)
num_symbols = random.randint(2, 4)
num_numbers = random.randint(2, 4)

wnd = Tk()
wnd.title("Password Manager")
wnd.config(padx=50, pady=30)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file=img_full_path)
canvas.create_image(125, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_text = Label(text="Website: ", font=(FONT_NAME, 10))
website_text.grid(row=1, column=0)

email_text = Label(text="Email/Username: ", font=(FONT_NAME, 10))
email_text.grid(row=2, column=0)

pswd_text = Label(text="Password: ", font=(FONT_NAME, 10))
pswd_text.grid(row=3, column=0)

website_entry = Entry(width=35,font=(FONT_NAME_2, 10))
website_entry.grid(row=1, column=1, columnspan=2,  sticky="EW")
website_entry.focus()

email_user_entry = Entry(width=35, font=(FONT_NAME_2, 10))
email_user_entry.insert(END, "email@gmail.com")
email_user_entry.grid(row=2, column=1, columnspan=2, sticky="EW")

password_entry = Entry(width=30,font=(FONT_NAME_2, 10))
password_entry.grid(row=3, column=1, sticky="W")

#=== ADD BUTTON ===
def add_password():
    website = website_entry.get()
    email = email_user_entry.get()
    password = password_entry.get()
    if website =="" or email=="" or password=="":
        messagebox.showinfo(title="Error", message="Please fill all fields.")
    else:
        if confirm_entry(website, email, password):
            save_info(website, email, password)

#=== GENERATE PWD BUTTON ===
def generate_password():
    letters_password = [random.choice(letters) for _ in range(num_letters)]
    symbols_password = [random.choice(symbols) for _ in range(num_symbols)]
    numbers_password = [random.choice(numbers) for _ in range(num_numbers)]
    password_list = letters_password + symbols_password + numbers_password
    random.shuffle(password_list)
    print(password_list)
    new_password = "".join(password_list)
    password_entry.insert(END, new_password)
    put_password_in_paperclip(new_password)

#=== Save in TXT ===
def save_info(website, email, password):
    with open("MyFile.txt", "a") as file:
        file.write(f"{website} | {email} | {password}\n")
    website_entry.delete(0, END)
    password_entry.delete(0, END)

#--- Confirm data entry ---
def confirm_entry(website, email, password):
    choice = messagebox.askokcancel(title=website, message=f"These are the details entered: \n Email: {email}, \n Password: {password} \n Is it ok to save?")
    return choice

# ---Paper Clip using pip install paper ---
def put_password_in_paperclip(password):
    print("Copying password")
    pyperclip.copy(password)

generate_passw_btn = Button(text="Generate Password", font=(FONT_NAME, 10), command=generate_password)
generate_passw_btn.grid(row=3, column=2)

add_btn = Button(text="Add", font=(FONT_NAME, 10), command=add_password)
add_btn.grid(row=4, column=1, columnspan=2, sticky="EW")

wnd.mainloop(
