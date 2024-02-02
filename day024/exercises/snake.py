from turtle import Turtle

ANGLES = {
    "EAST": 0,
    "NORTH": 90,
    "WEST": 180,
    "SOUTH": 270
}
STARTING_SEGMENTS = 3


class Snake:

    def __init__(self, segment_size):
        self.segment_size = segment_size
        self.segments = []
        self.direction = ANGLES["EAST"]
        self.create_start_snake()
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
        self.segments.append(t)

    def create_start_snake(self):
        for i in range(STARTING_SEGMENTS):
            self.create_snake_body_part(-i * self.segment_size, 0)

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
        """
        Change snake direction to move up
        """
        if self.direction is not ANGLES["SOUTH"]:
            self.direction = ANGLES["NORTH"]

    def down(self):
        """
        Change snake direction to move down
        """
        if self.direction is not ANGLES["NORTH"]:
            self.direction = ANGLES["SOUTH"]

    def left(self):
        """
        Change snake direction to move left
        """
        if self.direction is not ANGLES["EAST"]:
            self.direction = ANGLES["WEST"]

    def right(self):
        """
        Change snake direction to move right
        """
        if self.direction is not ANGLES["WEST"]:
            self.direction = ANGLES["EAST"]

    def get_tail(self):
        """
        Get last segment of snake
        """
        return self.segments[-1]

    def grow(self):
        """
        Add segment to snake at the tail
        """
        tail = self.get_tail()
        new_x = tail.xcor()
        new_y = tail.ycor()
        self.create_snake_body_part(new_x, new_y)

    def reset(self):
        for segment in self.segments:
            segment.clear()
            segment.hideturtle()
        self.segments.clear()
        self.create_start_snake()
        self.direction = ANGLES["EAST"]
        self.head = self.segments[0]
