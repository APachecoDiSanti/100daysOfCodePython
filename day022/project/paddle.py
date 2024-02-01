from turtle import Turtle

PADDLE_HEIGHT = 100
PADDLE_WIDTH = 20
TILE_SIZE = 20
UP = 90
DOWN = 270
STEP_SIZE = 10


class Paddle(Turtle):

    def __init__(self, start_x, screen_height):
        super().__init__()
        self.screen_height = screen_height
        self.speed("fastest")
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=PADDLE_HEIGHT//TILE_SIZE, stretch_len=PADDLE_WIDTH//TILE_SIZE)
        self.setx(start_x)
        self.sety(0)

    def up(self):
        """
        Move paddle up unless it would go above screen
        """
        if self.ycor() < self.screen_height//2 - PADDLE_HEIGHT//2:
            self.sety(self.ycor()+STEP_SIZE)

    def down(self):
        """
        Move paddle down unless it would go below screen
        """
        if self.ycor() > -self.screen_height//2 + PADDLE_HEIGHT//2:
            self.sety(self.ycor()-STEP_SIZE)

    def collision_distance(self):
        """
        Return the distance threshold that we will use when checking collision with a paddle
        """
        return PADDLE_HEIGHT//2
