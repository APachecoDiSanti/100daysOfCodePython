from turtle import Turtle

ALIGNMENT = "center"
FONT_SIZE = 24
FONT = ("Arial", FONT_SIZE, "normal")


class Scoreboard(Turtle):

    def __init__(self, screen_size, tile_size):
        super().__init__()
        # Attributes
        self.score = 0
        self.y_position = screen_size // 2 - tile_size - FONT_SIZE

        self.show_score()

    def show_score(self):
        """
        Displays the current score
        """
        self.reset()
        self.hideturtle()
        self.sety(self.y_position)
        self.color("white")
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """
        Increases score and shows it on screen
        """
        self.score += 1
        self.show_score()

    def game_over(self):
        """
        Show game over to player
        """
        self.sety(0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
