import os
from tkinter import *
import requests

FONT_NAME = "Times New Roman"
ninja_path = os.path.join("utils", "ninja1.png")
current_dir = os.getcwd()
ninja_full_path = os.path.join(current_dir, ninja_path)
API_KEY = "c0EebPPBPVnxMb0tjhfnScJg3PKEU87d5lBt2m74"


window = Tk()
window.title("Random Quote Generator")
window.config(padx = 40, pady = 10, background = "black")

canvas = Canvas(window, width=800, height=600, background="black", highlightthickness=0)
quote_txt = canvas.create_text(600, 300, text="", width=250, fill="white", font=(FONT_NAME, 20, "bold"))
autor_txt = canvas.create_text(550, 500, text="", width=250, fill="white", font=(FONT_NAME, 15, "italic"))
canvas.grid(row=2, column=1, columnspan=2)
photo_img = PhotoImage(file=ninja_full_path)
canvas.create_image(200,300, image=photo_img)



def get_quote():
    """calls an api to retrieve randomly generated quotes"""
    response = requests.get(url="https://api.api-ninjas.com/v2/randomquotes?categories=success,wisdom", headers={"X-Api-Key": API_KEY})
    data = response.json()
    print(data)
    quote = data[0]["quote"]
    author = data[0]["author"]
    canvas.itemconfig(quote_txt, text=quote)
    canvas.itemconfig(autor_txt, text=f"-{author}")

get_quote()



window.mainloop()