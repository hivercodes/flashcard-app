from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
df = pandas.read_csv("data/french_words.csv")
data_dict = df.to_dict(orient="records")

first_run = 1
word_dict = {}
print(data_dict)
def timer():
    window.after(3000, next_answer)



def button_press():
    pass



def new_word():
    global first_run
    first_run = 0
    global word_dict
    new_index = random.randint(0, len(df) - 1)
    word_dict = data_dict[new_index]
    canvas.itemconfig(canvas_image, image=front_image)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=word_dict["French"], fill="black")
    timer()


def remove_from_list():
    for item in data_dict:
        if item == word_dict:
            data_dict.pop(data_dict.index(word_dict))
    new_word()



def next_answer():
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=word_dict["English"], fill="white")
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

success_button = Button(image=success_image, highlightthickness=0, command=remove_from_list)
success_button.grid(column=1, row=1)





if first_run == 1:
    new_word()



timer()









window.mainloop()