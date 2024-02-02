import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

MAX_COORDINATE = 300

screen = Screen()
screen.setup(width=MAX_COORDINATE*2, height=MAX_COORDINATE*2, startx=0, starty=0)
screen.tracer(0)

player = Player(MAX_COORDINATE)
scoreboard = Scoreboard(MAX_COORDINATE)
car_manager = CarManager(MAX_COORDINATE)

screen.listen()
screen.onkey(key="w", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.maybe_create_car()
    car_manager.blacklist_cars()
    car_manager.move_cars()
    if player.has_reached_finish_line(MAX_COORDINATE):
        scoreboard.next_level()
        car_manager.next_level()
        player.reset_player(MAX_COORDINATE)
    if car_manager.player_collided_with_car(player):
        scoreboard.game_over()
        game_is_on = False
    screen.update()

screen.exitonclick()
