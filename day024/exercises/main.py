from snake import Snake
from food import Food
from scoreboard import Scoreboard

from turtle import Screen
import time

SCREEN_SIZE = 600
TILE_SIZE = 20
MAX_POSITION = SCREEN_SIZE // 2 - TILE_SIZE


def setup_screen(in_snake):
    """
    Return a screen that is SCREEN_SIZE x SCREEN_SIZE and with black background.
    """
    s = Screen()
    s.setup(width=SCREEN_SIZE, height=SCREEN_SIZE, startx=0, starty=0)
    s.bgcolor("black")
    s.title("Snake")
    s.tracer(0)
    s.listen()
    s.onkey(in_snake.up, "w")
    s.onkey(in_snake.down, "s")
    s.onkey(in_snake.left, "a")
    s.onkey(in_snake.right, "d")
    return s


# START
snake = Snake(TILE_SIZE)
screen = setup_screen(snake)
food = Food(SCREEN_SIZE, TILE_SIZE)
scoreboard = Scoreboard(SCREEN_SIZE, TILE_SIZE)

speed_s = 0.1
is_game_running = True
while is_game_running:
    snake.move()
    screen.update()
    time.sleep(speed_s)

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.grow()

    if abs(snake.head.xcor()) > MAX_POSITION or abs(snake.head.ycor()) > MAX_POSITION:
        scoreboard.reset_score()
        snake.reset()

    for segment in snake.segments[1:]:
        if is_game_running and snake.head.distance(segment) < 15:
            scoreboard.reset_score()
            snake.reset()

screen.exitonclick()
