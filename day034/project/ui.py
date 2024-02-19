from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class GridWidget:

    def __init__(self, widget, columnspan=1, pady=0):
        self.widget = widget
        self.columnspan = columnspan
        self.pady = pady


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.label_score = Label(text="Score: 0", font=("Arial", 20), fg="white", bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas_question = self.canvas.create_text(150, 125, text="", font=("Arial", 20, "bold"), fill=THEME_COLOR, width=280)

        image_true = PhotoImage(file="images/true.png")
        self.button_true = Button(image=image_true, highlightthickness=0, command=self.check_answer_is_true)

        false_image = PhotoImage(file="images/false.png")
        self.button_false = Button(image=false_image, highlightthickness=0, command=self.check_answer_is_false)

        label_score_gw = GridWidget(self.label_score)
        canvas_gw = GridWidget(self.canvas, columnspan=2, pady=50)
        button_true_gw = GridWidget(self.button_true)
        button_false_gw = GridWidget(self.button_false)

        layout = [
            [None, label_score_gw],
            [canvas_gw],
            [button_true_gw, button_false_gw]
        ]
        self.apply_grid_layout(layout)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.label_score.config(text=f"Score: {self.quiz.score}")
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_question, text=question, fill=THEME_COLOR)
        else:
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")
            self.canvas.itemconfig(self.canvas_question, text=f"Final score:\n{self.quiz.score}/{len(self.quiz.question_list)}", fill=THEME_COLOR)

    def check_answer_is_true(self):
        is_correct = self.quiz.check_answer("true")
        if is_correct is None:
            pass
        elif is_correct:
            self.canvas.config(bg="green")
            self.canvas.itemconfig(self.canvas_question, fill="white")
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.canvas_question, fill="white")
            self.window.after(1000, self.get_next_question)

    def check_answer_is_false(self):
        is_correct = self.quiz.check_answer("false")
        if is_correct is None:
            pass
        elif is_correct:
            self.canvas.config(bg="green")
            self.canvas.itemconfig(self.canvas_question, fill="white")
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.canvas_question, fill="white")
            self.window.after(1000, self.get_next_question)

    def apply_grid_layout(self, grid_layout):
        for row in range(len(grid_layout)):
            for column in range(len(grid_layout[row])):
                ui_widget = grid_layout[row][column]
                if ui_widget is not None:
                    ui_widget.widget.grid(row=row, column=column, columnspan=ui_widget.columnspan, pady=ui_widget.pady)
