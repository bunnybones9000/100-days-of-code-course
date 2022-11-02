import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
FONT = ("Ariel", 40, "italic")
french_data_frame = pandas.read_csv('data/french_words.csv')
french_dict = french_data_frame.to_dict(orient="records")
current_card = {}
# ------------------------------------------ flip cards Functions -------------------------------------- #


def next_card():
    global current_card, flip_timer
    windows.after_cancel(flip_timer)
    current_card = random.choice(french_dict)

    canvas.itemconfig(image, image=card_front)
    canvas.itemconfig(title, text="French", fill='black')
    canvas.itemconfig(word, text=current_card['French'], fill='black')

    flip_timer = windows.after(3000, to_english)


def to_english():
    canvas.itemconfig(image, image=card_back)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card['English'], fill='white')


# -------------------------------------------- UI ------------------------------------------------ #
windows = Tk()
windows.config(padx=50, pady=50, bg=BACKGROUND_COLOR, highlightthickness=0)
windows.title("FLASH CARDS")

flip_timer = windows.after(3000, to_english)

card_front = PhotoImage(file='C:/Users/USER/PycharmProjects/Day-31/images/card_front.png')
card_back = PhotoImage(file="C:/Users/USER/PycharmProjects/Day-31/images/card_back.png")

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
image = canvas.create_image(405, 263, image=card_front)
title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2,)


right_image = PhotoImage(file="C:/Users/USER/PycharmProjects/Day-31/images/right.png")
right_button = Button(image=right_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=0, columnspan=2)


next_card()
windows.mainloop()
