from turtle import Turtle

EAST = 180


class Car(Turtle):

    def __init__(self, speed, color, start_x, start_y):
        super().__init__()
        self.color(color)
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=2)
        self.setx(start_x)
        self.sety(start_y)
        self.setheading(EAST)
        self.speed = speed

    def move(self):
        """
        Move car forward
        """
        self.forward(self.speed)
