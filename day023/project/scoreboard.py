from turtle import Turtle

FONT_SIZE = 24
FONT = ("Courier", FONT_SIZE, "normal")


class Scoreboard(Turtle):

    def __init__(self, max_coordinate):
        super().__init__()
        self.level = 1
        self.setx(-max_coordinate + FONT_SIZE * 7)
        self.sety(max_coordinate - FONT_SIZE * 2)
        self.show_level()

    def show_level(self):
        """
        Display current level
        """
        new_x = self.xcor()
        new_y = self.ycor()
        self.reset()
        self.penup()
        self.hideturtle()
        self.setx(new_x)
        self.sety(new_y)
        self.write(f"Level: {self.level}", align="right", font=FONT)

    def next_level(self):
        """
        Increase current level and display it on screen
        """
        self.level += 1
        self.show_level()

    def game_over(self):
        """
        Display game over
        """
        self.setx(0)
        self.sety(-self.ycor())
        self.write("GAME OVER", align="center", font=FONT)
