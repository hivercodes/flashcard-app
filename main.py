from tkinter import *


BACKGROUND_COLOR = "#B1DDC6"


window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50)
window.config(bg=BACKGROUND_COLOR)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=850, height=600, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.create_image(425, 300, image=front_image)
language_text = canvas.create_text(400,150, text="language", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, rowspan=2)
























window.mainloop()