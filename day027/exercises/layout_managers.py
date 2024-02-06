from tkinter import *


def button_clicked():
    my_label["text"] = input.get()


window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="This is a label", font=("Arial", 24, "bold"))
my_label["text"] = "New text"
# my_label.place(x=100, y=10)
my_label.grid(column=0, row=0)


# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New button")
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=10)
input.grid(column=3, row=2)

# This line should always be at the end of the file
window.mainloop()
