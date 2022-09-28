from tkinter import*
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pd.read_csv("./data/words_to_learn.csv")
except:
    original_data = pd.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient='records')



def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_title,text="French",fill="black")
    canvas.itemconfig(canvas_word,text=current_card["French"],fill="black")
    canvas.itemconfig(canvas_image,image=photo_image)
    flip_timer = window.after(3000, func=flip_card)



def flip_card():
    canvas.itemconfig(canvas_title,text="English",fill="white")
    canvas.itemconfig(canvas_word,text=current_card["English"],fill="white")
    canvas.itemconfig(canvas_image,image=reverse_image)

def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv",index=False)

    next_card()

#----------------------UI------------------------
window = Tk()
window.title("Flash Card")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
photo_image = PhotoImage(file="./images/card_front.png")
reverse_image = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400,263,image=photo_image)
canvas_title = canvas.create_text(400,150,text="",font=("Arial",40,"italic"))
canvas_word = canvas.create_text(400,263,text="",font=("Arial",60,"italic"))
canvas.grid(row=0,column=0,columnspan=2)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image,highlightthickness=0,command=next_card)
wrong_button.grid(row=1,column=0)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image,highlightthickness=0,command=is_known)
right_button.grid(row=1,column=1)

next_card()

window.mainloop()

