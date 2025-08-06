"""
main.py
"""
from tkinter import *
import pandas as pd
import random

# ------------------------------ CONSTANTS ------------------------ #
GREEN = '#228B22'
WORD_FONT = ('Arial', 60, 'bold')
TITLE_FONT = ('Arial', 40, 'italic')

# ------------------------------- FUNCTIONALITY --------------------- #
# Retrieve data from word_bank.csv
try:
    df = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    df = pd.read_csv('data/word_bank.csv')

data = df.to_dict('records')

# Pick random word
word = random.choice(data)

def correct():
    """What to do when user is correct."""
    global word
    global data

    data.remove(word)
    # Create a new dataframe from current records
    df = pd.DataFrame.from_records(data)
    df.to_csv("data/words_to_learn.csv", index=False)

    # Get the next card
    next_card()

def next_card():
    """Select a new random Hausa word"""
    global word
    global after_id

    if after_id is not None:
        canvas.after_cancel(after_id)

    word = random.choice(data)
    # Display on canvas
    canvas.itemconfigure(display_img, image=front_img)
    canvas.itemconfigure(display_title, text="Hausa", fill="black")
    canvas.itemconfigure(display_word, text=word["Hausa"], fill="black")

    # Flip after three seconds
    after_id = canvas.after(3000, flip_card)

def flip_card():
    """Flip current card to show the English meaning."""
    global word
    canvas.itemconfigure(display_img, image=back_img)
    canvas.itemconfigure(display_title, text="English", fill="white")
    canvas.itemconfigure(display_word, text=word["English"], fill="white")


# ------------------------------ UI SETUP ------------------------- #
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=GREEN)

# Canvas
canvas = Canvas(width=800, height=525)
# front & back card images
front_img = PhotoImage(file='images/front.png')
back_img = PhotoImage(file='images/back.png')

# Elements on canvas widget.
display_img = canvas.create_image(402, 265, image=front_img)
display_title = canvas.create_text(402, 132.5, text="Hausa", font=TITLE_FONT)
display_word = canvas.create_text(402, 265, text=word["Hausa"], font=WORD_FONT)

# flip card after the first 3 seconds
after_id = canvas.after(3000, flip_card)

canvas.grid(row=0, column=0, columnspan=2, pady=10)

# Buttons
wrong_image = PhotoImage(file='images/wrong.png')
wrong_btn = Button(image=wrong_image, highlightthickness=0,
                   relief="flat", borderwidth=0,
                   command=next_card)
wrong_btn.grid(row=1, column=0)

correct_image = PhotoImage(file='images/correct.png')
correct_btn = Button(image=correct_image, highlightthickness=0,
                     relief="flat", borderwidth=0,
                     command=correct)
correct_btn.grid(row=1, column=1)

window.mainloop()