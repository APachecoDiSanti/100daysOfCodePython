from turtle import Turtle


FONT_SIZE = 40
FONT = ("Courier", FONT_SIZE, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self, screen_height):
        super().__init__()
        self.start_y_position = screen_height // 2 - FONT_SIZE*2
        self.left_score = 0
        self.right_score = 0
        self.show_score()

    def show_score(self):
        """
        Display score of both players
        """
        self.reset()
        self.penup()
        self.hideturtle()
        self.sety(self.start_y_position)
        self.color("white")
        self.write(f"{self.left_score} - {self.right_score}", align=ALIGNMENT, font=FONT)

    def increase_left_score(self):
        """
        Increase score of left player
        """
        self.left_score += 1
        self.show_score()

    def increase_right_score(self):
        """
        Increase score of right player
        """
        self.right_score += 1
        self.show_score()
