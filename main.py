from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FR_WORD_KEY = 'French'
EN_WORD_KEY = 'English'
timer = None
currentCard = {}

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
wordList = data.to_dict(orient="records")


def isKnown():
    wordList.remove(currentCard)
    dfWordList = pandas.DataFrame(wordList)
    dfWordList.to_csv("./data/words_to_learn.csv", index=False)


def rightButtonClick():
    window.after_cancel(timer)
    nextCard()
    isKnown()


def wrongButtonClick():
    window.after_cancel(timer)
    nextCard()


def nextCard():
    global currentCard
    currentCard = random.choice(wordList)
    canvas.itemconfig(titleText, text=FR_WORD_KEY, fill="black")
    canvas.itemconfig(wordText, text=currentCard[FR_WORD_KEY], fill="black")
    canvas.itemconfig(cardImage, image=cardFront)
    global timer
    timer = window.after(3000, flipCard)


def flipCard():
    canvas.itemconfig(titleText, text=EN_WORD_KEY, fill="white")
    canvas.itemconfig(wordText, text=currentCard[EN_WORD_KEY], fill="white")
    canvas.itemconfig(cardImage, image=cardBack)


window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
cardFront = PhotoImage(file="./images/card_front.png")
cardBack = PhotoImage(file="./images/card_back.png")
cardImage = canvas.create_image(400, 263, image=cardFront)
titleText = canvas.create_text(400, 150, text="Title", font=("Arial", 30, "italic"))
wordText = canvas.create_text(400, 263, text="Word", font=("Arial", 50, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

rightImg = PhotoImage(file="./images/right.png")
wrongImg = PhotoImage(file="./images/wrong.png")
rightButton = Button(image=rightImg, highlightthickness=0, command=rightButtonClick)
rightButton.grid(column=1, row=1)
wrongButton = Button(image=wrongImg, highlightthickness=0, command=wrongButtonClick)
wrongButton.grid(column=0, row=1)

nextCard()

window.mainloop()
