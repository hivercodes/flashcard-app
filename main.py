from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
df = pandas.read_csv("data/french_words.csv")
data_dict = df.to_dict(orient="records")

first_run = 1

def button_press():
    pass



def new_word():
    global first_run
    first_run = 0
    new_index = random.randint(0, len(df)-1)
    word_dict = data_dict[new_index]
    canvas.itemconfig(word_text, text=word_dict["French"])




def next_answer(word_dict):
    canvas.itemconfig(word_text, text=word_dict["English"])
    canvas.itemconfig(canvas_image, image=back_image)






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
canvas_image = canvas.create_image(400, 263, image=front_image)
language_text = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

#buttons
wrong_button = Button(image=fail_image, highlightthickness=0, command=new_word)
wrong_button.grid(column=0, row=1)

success_button = Button(image=success_image, highlightthickness=0, command=new_word)
success_button.grid(column=1, row=1)





if first_run == 1:
    new_word()













window.mainloop()