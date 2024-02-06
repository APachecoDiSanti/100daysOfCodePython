import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="This is a label", font=("Arial", 24, "bold"))
my_label.pack(side="left")

# This line should always be at the end of the file
window.mainloop()
