from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_SIZE = 20
LEFT_START = -SCREEN_WIDTH//2+TILE_SIZE*2
RIGHT_START = SCREEN_WIDTH//2-TILE_SIZE*2
LEFT_EDGE = -SCREEN_WIDTH // 2
RIGHT_EDGE = SCREEN_WIDTH // 2
SPEED = 0.1


def setup_screen():
    """
    Initialize screen for the game
    """
    s = Screen()
    s.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, startx=0, starty=0)
    s.bgcolor("black")
    s.title("Pong")
    s.listen()
    s.tracer(0)
    return s


# START
screen = setup_screen()

# Player 1
left_paddle = Paddle(LEFT_START, SCREEN_HEIGHT)
screen.onkey(key="w", fun=left_paddle.up)
screen.onkey(key="s", fun=left_paddle.down)

# Player 2
right_paddle = Paddle(RIGHT_START, SCREEN_HEIGHT)
screen.onkey(key="i", fun=right_paddle.up)
screen.onkey(key="k", fun=right_paddle.down)

ball = Ball()
scoreboard = Scoreboard(SCREEN_HEIGHT)

# Game loop
is_game_running = True
while is_game_running:
    time.sleep(SPEED)
    if ball.is_colliding_with_wall(SCREEN_HEIGHT):
        ball.bounce_wall()
    if ball.is_colliding_with_paddle(right_paddle):
        ball.bounce_paddle()
    if ball.is_colliding_with_paddle(left_paddle):
        ball.bounce_paddle()
    if ball.xcor() > RIGHT_EDGE:
        scoreboard.increase_left_score()
        ball.reset_left()
    if ball.xcor() < LEFT_EDGE:
        scoreboard.increase_right_score()
        ball.reset_right()
    ball.move()
    screen.update()

screen.exitonclick()
