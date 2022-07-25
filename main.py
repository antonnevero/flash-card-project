from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
WORK_SEC = 3

# ---------------------RANDOM_WORD--------------------
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/English_words.csv")
    word_list = data.to_dict(orient="records")
else:
    word_list = data.to_dict(orient="records")
finally:
    current_card = {}


def random_word():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(word_list)
    canvas.itemconfig(title, text="English", fill="black")
    canvas.itemconfig(word, text=current_card['English'], fill="black")
    canvas.itemconfig(canvas_image, image=card_front_image)
    timer = window.after(3000, func=change_card)

# -----------------CHANGE_CARD------------------------


def change_card():
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(title, text="Ukrainian", fill="white")
    canvas.itemconfig(word, text=current_card["Ukrainian"], fill="white")

# ---------------------REMOVE_CARDS-------------------


def remove_cards():
    word_list.remove(current_card)
    df = pandas.DataFrame.from_dict(word_list)
    df.to_csv("data/words_to_learn.csv", index=False)
    random_word()

# ---------------------UI-----------------------------


window = Tk()
window.title("En to Ua")
window.config(bg=BACKGROUND_COLOR)
window.config(padx=50, pady=50)

timer = window.after(3000, func=change_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_image)
title = canvas.create_text(400, 150, text="", font=LANGUAGE_FONT)
word = canvas.create_text(400, 263, text="", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, borderwidth=1, command=remove_cards)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, borderwidth=1, command=random_word)
wrong_button.grid(row=1, column=0)

random_word()


window.mainloop()
