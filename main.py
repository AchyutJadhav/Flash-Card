from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"


# functions
try:
    data = pandas.read_csv("data/word_to_learn.csv")
    data_dic = data.to_dict(orient="records")

except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    data_dic = data.to_dict(orient="records")

new_word = {}


def change_word():
    global new_word, timer
    window.after_cancel(timer)
    new_word = random.choice(data_dic)
    new_french_word = new_word["French"]
    canvas.itemconfig(word, text=new_french_word, fill="black")
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(image, image=front_image)
    timer = window.after(3000, func=flip_card)


def flip_card():
    new_english_word = new_word["English"]
    canvas.itemconfig(word, text=new_english_word, fill="white")
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(image, image=back_image)
    # data_dic.remove(new_word)
    # save_dict = {'French':  new_french_word, 'English': new_english_word}
    # data.to_csv("new_data.csv")


def is_known():
    data_dic.remove(new_word)
    print(len(data_dic))
    new_data = pandas.DataFrame(data_dic)
    new_data.to_csv("data/word_to_learn.csv", index=False)
    change_word()


# window create
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, func=flip_card)


# canvas
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
image = canvas.create_image(400, 263, image=front_image)
canvas.grid(row=0, column=0, columnspan=2)
language = canvas.create_text(400, 150, text="Language", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 300, text="Word", font=("Arial", 60, "bold"))


# button
right_image = PhotoImage(file="images/right.png")
right = Button(image=right_image, highlightthickness=0, command=is_known)
right.grid(row=1, column=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong = Button(image=wrong_image, highlightthickness=0, command=change_word)
wrong.grid(row=1, column=0)

change_word()

mainloop()
