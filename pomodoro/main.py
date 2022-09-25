from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    #timer_text 00:00
    canvas.itemconfig(timer_text, text="00:00")
    #title_label "Timer"
    timer_label.config(text="Timer")
    #reset check_marks
    mark = ""
    check_label.config(text=mark)
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 != 0:
        timer_label.config(text="Working~~",fg=RED)
        count_down(work_sec)
    elif reps % 2 == 0 and reps != 8:
        timer_label.config(text="Short Break~~",fg=PINK)
        count_down(short_break_sec)
    elif reps == 8:
        timer_label.config(text="Long Break~~",fg=PINK)
        count_down(long_break_sec)
        reps = 0


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        check_label.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)
#count_down(5)

#Label
timer_label = Label(text="Timer",font=("Arial",28,"bold"),bg=YELLOW,fg=GREEN)
timer_label.grid(row=0,column=1)

#Button
start_button = Button(text="start",highlightthickness=0,command=start_timer)
start_button.grid(row=2,column=0)
reset_button = Button(text="reset",highlightthickness=0,command=reset_timer)
reset_button.grid(row=2,column=2)


check_label = Label(bg=YELLOW)
check_label.grid(row=3,column=1)




window.mainloop()