from tkinter import *

CONVERSION_FACTOR = 1.609


window = Tk()
window.title("My First GUI")
window.minsize(width=500, height=300)
window.configure(background="white")
window.config(padx=20, pady=20)

new_label = Label(text="Conversion Tool", font=("Times New Roman", 20, "bold"), cursor="arrow")
new_label.grid(row=0, column=2)
new_label.config(padx=10, pady=20, background="white",fg="black")

lbl_km = Label(text="Kilometers", font=("Times New Roman", 12))
#lbl_km.place(x=100, y=100)
#lbl_km.pack(side="left")
lbl_km.grid(row=3, column=0)
lbl_km.config(background="white",fg="black")

lbl_miles = Label(text="Miles", font=("Times New Roman", 12))
#lbl_miles.pack(side="left")
lbl_miles.grid(row=4, column=0)
lbl_miles.config(background="white",fg="black")

#Entry
input_km = Entry(width=10)
input_km.grid(row=3, column=1)

input_miles = Entry(width=10)
input_miles.grid(row=4, column=1)


def convert_to_km():
    arr = input_miles.get().split(".")[0]
    print(arr)
    miles_input= float(input_miles.get())
    result = str(calculate_miles(miles_input))
    result_to_km.config(text=result)
    result_to_km.grid(row=4, column=5)
    result_to_km.config(background="white", fg="black")

def convert_to_miles():
    km_input = float(input_km.get())
    result = str(calculate_km(km_input))
    lbl_result.config(text=result)
    lbl_result.grid(row=3, column=5)
    lbl_result.config(background="white", fg="black")

def calculate_km(miles):
    return round(miles/CONVERSION_FACTOR, 2)

def calculate_miles(km):
    return round(km*CONVERSION_FACTOR,2)

def clear():
    input_km.delete(0, END)
    input_miles.delete(0, END)
    result_to_km.config(text="   ")
    lbl_result.config(text="   ")

result_to_km = (Label(text="", font=("Times New Roman", 12, "bold")))
lbl_result = Label(text="", font=("Times New Roman", 12, "bold"))

btn_to_miles = Button(text= "Convert to Miles",command=convert_to_miles)
btn_to_miles.grid(row=3, column=2)

btn_to_km = Button(text= "Convert to Km",command=convert_to_km)
btn_to_km.grid(row=4, column=2)

btn_to_km = Button(text= "Clear",command=clear)
btn_to_km.grid(row=5, column=2)

window.mainloop()

