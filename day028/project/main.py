from tkinter import *
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
    timer_label.config(text="Timer", fg="#000000")
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    if reps % 2 == 0:
        minutes = WORK_MIN
        work_label()
    elif reps % 8 == 7:
        minutes = LONG_BREAK_MIN
        long_break_label()
    else:
        minutes = SHORT_BREAK_MIN
        short_break_label()
    count_down(minutes * 60)
    reps += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = count // 60
    seconds = count % 60
    time = f"{minutes}".rjust(2, "0") + ":" + f"{seconds}".rjust(2, "0")
    canvas.itemconfig(timer_text, text=time)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        global reps
        if reps % 2 == 0:
            checkmarks = checkmark_label.cget("text")
            checkmark_label.config(text=checkmarks + "✓")

# ---------------------------- UI SETUP ------------------------------- #
def work_label():
    timer_label.config(text="Work", fg=GREEN)

def short_break_label():
    timer_label.config(text="Break", fg=PINK)

def long_break_label():
    timer_label.config(text="Break", fg=RED)

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 50), bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

start_button = Button(text="Start", highlightthickness=0, command=start_timer)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)

checkmark_label = Label(font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)

layout = [
    [None,          timer_label,        None],
    [None,          canvas,             None],
    [start_button,  None,               reset_button],
    [None,          checkmark_label,    None]
]

for row in range(len(layout)):
    for column in range(len(layout[row])):
        widget = layout[row][column]
        if widget is not None:
            widget.grid(row=row, column=column)

window.mainloop()
