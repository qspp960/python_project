from tkinter import*


def button_clicked():
    mile = input.get()
    km = float(mile) * 1.6
    km = int(km)
    label_3.config(text=f"{km}")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300,height=200)
window.config(padx=20,pady=20)

# Entry
input = Entry(width=10)
input.grid(row=0,column=1)

# Label
label_1 = Label(text="Miles",font=("Arial",24,"bold"))
label_1.grid(row=0,column=2)
label_2 = Label(text="is equal to",font=("Arial",24,"bold"))
label_2.grid(row=1,column=0)
label_3 = Label(text="0",font=("Arial",24,"bold"))
label_3.grid(row=1,column=1)
label_4 = Label(text="Km",font=("Arial",24,"bold"))
label_4.grid(row=1,column=2)

# Button
button = Button(text="Calculate",command=button_clicked)
button.grid(row=2,column=1)




window.mainloop()