from turtle import Turtle

MOVE_DISTANCE = 10
PLAYER_LENGTH = 20
NORTH = 90


class Player(Turtle):

    def __init__(self, max_coordinate):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.shape("turtle")
        self.left(NORTH)
        self.reset_player(max_coordinate)

    def reset_player(self, max_coordinate):
        """
        Return player to starting position
        """
        self.setx(0)
        self.sety(-max_coordinate + PLAYER_LENGTH)

    def move(self):
        """
        Move player forward
        """
        self.forward(MOVE_DISTANCE)

    def has_reached_finish_line(self, max_coordinate):
        """
        Check if player has reached end of screen
        """
        return self.ycor() > (max_coordinate - PLAYER_LENGTH)
