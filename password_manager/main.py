from tkinter import*
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letter = [random.choice(letters) for i in range(nr_letters)]
    #for char in range(nr_letters):
    #  password_list.append(random.choice(letters))

    password_symbol = [random.choice(symbols) for i in range(nr_symbols)]
    #for char in range(nr_symbols):
    #  password_list += random.choice(symbols)

    password_number = [random.choice(numbers) for i in range(nr_numbers)]
    #for char in range(nr_numbers):
    #  password_list += random.choice(numbers)
    password_list = password_letter + password_symbol + password_number
    random.shuffle(password_list)

    password = "".join(password_list)
    #password = ""
    #for char in password_list:
    #  password += char
    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_button_clicked():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email": email,
            "password": password,
         }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",message="Please don't have any fields empty!")
    else:
        #is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered: \n"
        #                       f"Email:{email} \n Password:{password}\n Is it ok to save?")

        try:
            with open("information.json", "r") as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
        except:
            with open("information.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
        else:
            with open("information.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0,END)
            email_entry.delete(0,END)
            password_entry.delete(0,END)
            website_entry.focus()

def search_button_clicked():
    website = website_entry.get()
    email = ""
    password = ""
    try:
        with open("information.json","r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No Data File")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email: {email}\n Password: {password}")
            website_entry.delete(0,END)
        else:
            messagebox.showinfo(title="Error",message="No detail website exists")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("password manager")
window.config(padx=50,pady=50,bg='white')


canvas = Canvas(width=200,height=200,bg="white",highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(row=0,column=1)

website_label = Label(text="Website:",font=("Arial",8,"bold"),bg="white",fg="black")
website_label.grid(row=1,column=0)
email_label = Label(text="Email/Username:",font=("Arial",8,"bold"),bg="white",fg="black")
email_label.grid(row=2,column=0)
password_label = Label(text="Password:",font=("Arial",8,"bold"),bg="white",fg="black")
password_label.grid(row=3,column=0)

website_entry = Entry(width=21)
website_entry.grid(row=1,column=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"qspp@daum.net")
password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)

search_button = Button(text="Search",width=10,command=search_button_clicked)
search_button.grid(row=1,column=2)
password_button = Button(text="Generate Password",command=generate_password)
password_button.grid(row=3,column=2)

add_button = Button(text="add",width=36,command=add_button_clicked)
add_button.grid(row=4,column=1,columnspan=2)


window.mainloop()