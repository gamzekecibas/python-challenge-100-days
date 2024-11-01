from tkinter import *
from tkinter import messagebox as mb
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    lang_data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    lang_data = pd.read_csv("data/chinese_freq_words.csv")

to_learn = lang_data.to_dict(orient="records")

# Functions
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Chinese", fill='black')
    canvas.itemconfig(card_word, text=current_card["Chinese"], fill='black')
    canvas.itemconfig(card_background, image=front_bg_image)
    flip_timer = window.after(3000, func=flip_card)
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=back_bg_image)

def is_known():
    to_learn.remove(current_card)
    mb.showinfo(title="INFO", message=f"{len(to_learn)} words left to learn!")
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# Background
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)  ## in ms, 3 seconds delay

# Card Front
canvas = Canvas(width=800, height=526)
front_bg_image = PhotoImage(file="images/card_front.png")
back_bg_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=front_bg_image)

# Adjusted coordinates for card_title and card_word
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 350, text="", font=("Arial", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightbackground=BACKGROUND_COLOR,
                      command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightbackground=BACKGROUND_COLOR,
                      command=is_known)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()