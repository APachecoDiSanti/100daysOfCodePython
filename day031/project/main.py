from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
FNT_LANGUAGE = ("Arial", 40, "italic")
FNT_WORD = ("Arial", 40, "bold")


# ---------------------------- APP LOGIC ------------------------------ #
def load_random_word():
    if len(list_indices) > 0:
        index = random.choice(list_indices)
        row = dict_words[dict_words.index == index].to_dict()
        canvas.itemconfig(card, image=img_front)
        canvas.itemconfig(txt_language, fill="black", text="French")
        canvas.itemconfig(txt_word, fill="black", text=row["French"][index])
        global timer
        timer = window.after(3000, flip_card)
    else:
        canvas.itemconfig(card, image=img_front)
        canvas.itemconfig(txt_language, fill="black", text="You're done!")
        canvas.itemconfig(txt_word, fill="black", text="No more words.")


def flip_card():
    word = canvas.itemcget(txt_word, "text")
    row = dict_words[dict_words["French"] == word].to_dict()
    for key in row["English"].keys():
        canvas.itemconfig(card, image=img_back)
        canvas.itemconfig(txt_language, fill="white", text="English")
        canvas.itemconfig(txt_word, fill="white", text=row["English"][key])


def add_word_to_answered():
    if timer != "":
        window.after_cancel(timer)
    word = canvas.itemcget(txt_word, "text")
    row = dict_words[dict_words["French"] == word].to_dict()
    for key in row["French"].keys():
        list_indices.remove(key)
    # I got a bit lost since I decided to track what indices have been asked. The end result is what is expected but
    # the way Angela does it is way better and less prone to errors. I'm sticking with this because I'm learning.
    with open("data/words_to_learn.csv", "w") as words_to_learn:
        d = {}
        for index in list_indices:
            row = dict_words[dict_words.index == index].to_dict()
            d[index] = {"French": row["French"][index], "English": row["English"][index]}
        p = pandas.DataFrame(d).transpose()
        p.to_csv(words_to_learn, index=False)

    load_random_word()


# ---------------------------- UI SETUP ------------------------------- #
def apply_grid_layout(grid_layout):
    for row in range(len(grid_layout)):
        for column in range(len(grid_layout[row])):
            widget = grid_layout[row][column]
            if widget is not None:
                columnspan = grid_layout[row][column][1]
                widget[0].grid(row=row, column=column, columnspan=columnspan)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
img_back = PhotoImage(file="images/card_back.png")
img_front = PhotoImage(file="images/card_front.png")
card = canvas.create_image(400, 263)
txt_language = canvas.create_text(400, 150, font=FNT_LANGUAGE)
txt_word = canvas.create_text(400, 263, font=FNT_WORD)

img_no = PhotoImage(file="images/wrong.png")
img_yes = PhotoImage(file="images/right.png")
btn_no = Button(image=img_no, highlightthickness=0, relief=FLAT, bd=0, background=BACKGROUND_COLOR, command=load_random_word)
btn_yes = Button(image=img_yes, highlightthickness=0, relief=FLAT, bd=0, background=BACKGROUND_COLOR, command=add_word_to_answered)


# Tuples with widget and their columnspan
layout = [
    [(canvas, 2)],
    [(btn_no, 1),   (btn_yes, 1)]
]
apply_grid_layout(layout)

words_already_answered = []
try:
    dict_words = pandas.read_csv("data/words_to_learn.csv")
except (FileNotFoundError, pandas.errors.EmptyDataError):
    dict_words = pandas.read_csv("data/french_words.csv")
list_indices = list(range(0, len(dict_words)))
timer = ""
load_random_word()

window.mainloop()
