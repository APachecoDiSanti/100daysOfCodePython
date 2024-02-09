from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import string
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
LETTERS = list(string.ascii_letters)
NUMBERS = list(string.digits)
SYMBOLS = list(string.punctuation)


def generate_password():
    password_letters = [choice(LETTERS) for _ in range(randint(8, 10))]
    password_symbols = [choice(SYMBOLS) for _ in range(randint(2, 4))]
    password_numbers = [choice(NUMBERS) for _ in range(randint(2, 4))]

    password_characters = password_letters + password_symbols + password_numbers
    shuffle(password_characters)
    generated_password = "".join(password_characters)

    password_input.delete(0, END)
    password_input.insert(0, generated_password)
    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if website == "" or email == "" or password == "":
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        new_data = {
            website: {
                "email": email,
                "password": password
            }
        }
        try:
            with open("data.json", "r") as password_file:
                data = json.load(password_file)
                data.update(new_data)
        except FileNotFoundError:
            data = new_data
        with open("data.json", "w") as password_file:
            json.dump(data, password_file, indent=4)
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- SEARCH --------------------------------- #
def find_password():
    try:
        with open("data.json", "r") as password_file:
            data = json.load(password_file)
    except FileNotFoundError:
        messagebox.showerror(message="No Data file found!")
    else:
        try:
            website = website_input.get()
            if website != "":
                stored_credentials = data[website]
                email = stored_credentials["email"]
                password = stored_credentials["password"]
                messagebox.showinfo(message=f"Your credentials for {website}:\nEmail: {email}\nPassword: {password}")
            else:
                messagebox.showerror(message="Please enter a website first!")
        except KeyError:
            messagebox.showwarning(message="No details stored for this website!")


# ---------------------------- UI SETUP ------------------------------- #
def apply_grid_layout(grid_layout):
    for row in range(len(grid_layout)):
        for column in range(len(grid_layout[row])):
            widget = grid_layout[row][column]
            if widget is not None:
                columnspan = grid_layout[row][column][1]
                widget[0].grid(row=row, column=column, columnspan=columnspan)


window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 95, image=logo_image)

website_label = Label(text="Website:")
website_input = Entry(width=21)
website_input.focus()
search_button = Button(text="Search", command=find_password)

email_label = Label(text="Email/Username:")
email_input = Entry(width=35)
email_input.insert(0, "email@example.com")

password_label = Label(text="Password:")
password_input = Entry(width=21)
password_button = Button(text="Generate Password", command=generate_password)

add_button = Button(text="Add", width=36, command=save)

# Tuples with widget and their columnspan
layout = [
    [None,                  (canvas, 1)],
    [(website_label, 1),    (website_input, 1), (search_button, 1)],
    [(email_label, 1),      (email_input, 2)],
    [(password_label, 1),   (password_input, 1),   (password_button, 1)],
    [None,                  (add_button, 2)]
]
apply_grid_layout(layout)

window.mainloop()
