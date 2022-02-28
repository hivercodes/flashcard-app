from tkinter import *


BACKGROUND_COLOR = "#B1DDC6"

#window config
window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50)
window.config(bg=BACKGROUND_COLOR)

#Images
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
fail_image = PhotoImage(file="images/wrong.png")
success_image = PhotoImage(file="images/right.png")



#canvas config
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.create_image(400, 263, image=front_image)
language_text = canvas.create_text(400, 150, text="language", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

#buttons
wrong_button = Button(image=fail_image, highlightthickness=0)
wrong_button.grid(column=0, row=1)

success_button = Button(image=success_image, highlightthickness=0)
success_button.grid(column=1, row=1)























window.mainloop()