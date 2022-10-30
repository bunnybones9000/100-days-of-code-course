from tkinter import *

windows = Tk()
windows.title("miles to kilometer converter")
windows.minsize(width=400, height=200)
windows.config(padx=30, pady=30)


def convert():
    kilo = float(number.get()) * 1.6
    label_3.config(text=kilo)


new_label = Label(text= "is equal to", font=("Ariel", 18, "normal"))
new_label.grid(column=0, row=1)

label_2 = Label(text="MILES", font=("Ariel", 18, "normal"))
label_2.grid(column=2, row=0)


label_3 = Label(text=0, font=("Ariel", 18, "normal"))
label_3.grid(column=1, row=1)

label_4 = Label(text="KM", font=("Ariel", 18, "normal"))
label_4.grid(column=2, row=1)

number = Entry()
number.grid(column=1, row=0)
number.config()


button = Button(text="Calculate", command= convert)
button.grid(column=1, row=2)


windows.mainloop()