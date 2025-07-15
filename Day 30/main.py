from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json
import pyperclip
CONFIG_FILE = 'data.json'
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_entry.delete(0,END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_list = []
    [password_list.append(choice(letters)) for _ in range(randint(8, 10))]
    [password_list.append(choice(symbols)) for _ in range(randint(2, 4))]
    [password_list.append(choice(numbers)) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ------------------------------- SEARCH ----------------------------------- #
def search():
    website = web_entry.get().capitalize()
    try:
        with open (CONFIG_FILE) as file:
            data = json.load(file)
        if website in data.keys():
            password = data[website]['password']
            email = data[website]['email']
            messagebox.showinfo(title='info', message = f'For {website} your Password is\n {password}\n and your email is\n {email}')
        else:
            raise KeyError
    except (FileNotFoundError,KeyError, json.decoder.JSONDecodeError):
           messagebox.showinfo(title='info', message = f'No info found for {website}')
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    email = user_entry.get()
    password = password_entry.get()
    new_data = {
        website.capitalize():{
            "email":email,
            "password":password
        }
    }
    if check_len(website, 'website') and check_len(password, 'password'):
        try:
            with open(CONFIG_FILE) as data_file:
                data = json.load(data_file)
                data.update(new_data)
            with open(CONFIG_FILE, 'w') as file:
                json.dump(data, file, indent = 4)
        except (FileNotFoundError,json.decoder.JSONDecodeError):
            with open(CONFIG_FILE, 'w') as file:
                json.dump(new_data, file, indent = 4)           
        web_entry.delete(0,END)
        password_entry.delete(0,END)

            
def check_len(entry, label):
    if entry=='':
        messagebox.showinfo(title='empty field', message=f'You left the {label} empty!')
        return False
    return True
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx = 50, pady = 50)
window.title('Password Manager')
# Canvas
canvas = Canvas(width = 200, height = 200)
lock_image = PhotoImage(file='logo.png')
canvas.create_image(100,100,image = lock_image)
canvas.grid(column=1,row=0)

#Labels
website = Label(text = 'Website:')
website.grid(column=0,row=1)
user = Label(text='Email/Username:')
user.grid(column=0,row=2)
password_label = Label(text='Password:')
password_label.grid(column=0,row=3)
#Buttons
generate_password_B = Button(text = 'Generate Password', command=generate_password)
generate_password_B.grid(column=2,row=3)
search_B = Button(text = 'Search',width = 14, command=search)
search_B.grid(column=2,row=1)
add_B = Button(text='Add', width = 44, command= save)
add_B.grid(column=1,row=4, columnspan = 2)
#Entries
web_entry = Entry(width=33)
web_entry.grid(column=1,row=1)
web_entry.focus()
user_entry = Entry(width=52)
user_entry.grid(column=1,row=2, columnspan=  2)
user_entry.insert(0,'lorenzo@gmail.com')
password_entry = Entry(width = 33)
password_entry.grid(column=1,row=3)
window.mainloop()