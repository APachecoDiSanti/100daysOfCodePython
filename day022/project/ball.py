from turtle import Turtle

START_RIGHT = 45
START_LEFT = 135
BALL_SIZE = 10
STARTING_SPEED = 10
SPEED_INCREMENT = 3


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.color("white")
        self.shape("circle")
        self.setheading(START_RIGHT)
        self.move_speed = STARTING_SPEED

    def move(self):
        """
        Move ball forward move_speed pixels
        """
        self.forward(self.move_speed)

    def is_colliding_with_wall(self, screen_height):
        """
        Check if ball collided with wall
        """
        return abs(self.ycor()) > screen_height // 2 - BALL_SIZE * 2

    def bounce_wall(self):
        """
        Change ball direction to bounce from wall
        """
        self.setheading((360 - self.heading()) % 360)

    def bounce_paddle(self):
        """
        Change ball direction to bounce from paddle
        """
        self.setheading((360 - self.heading() + 180) % 360)
        self.move_speed += SPEED_INCREMENT

    def is_colliding_with_paddle(self, paddle):
        """
        Check if ball collided with any paddle
        """
        return abs(self.xcor()) > abs(paddle.xcor()) - BALL_SIZE * 2 and self.distance(paddle) < paddle.collision_distance()

    def reset_left(self):
        """
        Reset the ball to start from center and move towards LEFT player
        """
        self.setx(0)
        self.sety(0)
        self.move_speed = STARTING_SPEED
        self.setheading(START_LEFT)

    def reset_right(self):
        """
        Reset the ball to start from center and move towards RIGHT player
        """
        self.setx(0)
        self.sety(0)
        self.move_speed = STARTING_SPEED
        self.setheading(START_RIGHT)
