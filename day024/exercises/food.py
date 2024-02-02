from turtle import Turtle
import random as r


class Food(Turtle):

    def __init__(self, screen_size, tile_size):
        super().__init__()
        # Attributes
        self.tile_size = tile_size
        self.max_position = screen_size // 2 - self.tile_size

        self.penup()
        self.color("blue")
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """
        Move food to a random position
        """
        random_x = r.randint(-self.max_position, self.max_position)
        random_y = r.randint(-self.max_position, self.max_position)
        self.goto(random_x - random_x % self.tile_size, random_y - random_y % self.tile_size)

