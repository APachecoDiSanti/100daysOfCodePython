from snake import Snake

from turtle import Screen
import time

SCREEN_SIZE = 600
TILE_SIZE = 20


def setup_screen():
    """
    Return a screen that is SCREEN_SIZE x SCREEN_SIZE and with black background.
    """
    s = Screen()
    s.setup(width=SCREEN_SIZE, height=SCREEN_SIZE, startx=0, starty=0)
    s.bgcolor("black")
    s.title("Snake")
    s.tracer(0)
    return s


# START
screen = setup_screen()
snake = Snake(TILE_SIZE)
speed_s = 0.1

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

is_game_running = True
while is_game_running:
    snake.move()
    screen.update()
    time.sleep(speed_s)

screen.exitonclick()
