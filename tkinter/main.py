from tkinter import*


def button_clicked():
    #my_label["text"] = "I got clicked"
    print("I got clicked")
    my_label["text"] = input.get()


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)


#Label
my_label = Label(text="I am a Label",font=("Arial",24,"bold"))
my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.pack()

#Button
button = Button(text="Click Me",command=button_clicked)
button.pack()

#Entry
input = Entry(width=10)
input.pack()





window.mainloop()