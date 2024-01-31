from turtle import Turtle

ANGLES = {
    "EAST": 0,
    "NORTH": 90,
    "WEST": 180,
    "SOUTH": 270
}


class Snake:

    def __init__(self, segment_size):
        self.segment_size = segment_size
        self.segments = []
        self.direction = ANGLES["EAST"]
        for i in range(3):
            t = self.create_snake_body_part(-i * self.segment_size, 0)
            self.segments.append(t)
        self.head = self.segments[0]

    def create_snake_body_part(self, x_pos, y_pos):
        """
        Create snake body part at (x_pos, y_pos)
        """
        t = Turtle("square")
        t.color("white")
        t.penup()
        t.setx(x_pos)
        t.sety(y_pos)
        return t

    def move(self):
        """
        Move the snake segments forward 1 tile from head to end
        """
        number_of_segments = len(self.segments)
        # Move body
        for i in range(number_of_segments - 1, 0, -1):
            self.segments[i].setx(self.segments[i - 1].xcor())
            self.segments[i].sety(self.segments[i - 1].ycor())
        # Move head
        self.head.setheading(self.direction)
        self.head.forward(self.segment_size)

    def up(self):
        if self.direction is not ANGLES["SOUTH"]:
            self.direction = ANGLES["NORTH"]

    def down(self):
        if self.direction is not ANGLES["NORTH"]:
            self.direction = ANGLES["SOUTH"]

    def left(self):
        if self.direction is not ANGLES["EAST"]:
            self.direction = ANGLES["WEST"]

    def right(self):
        if self.direction is not ANGLES["WEST"]:
            self.direction = ANGLES["EAST"]
