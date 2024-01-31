# WASD tank controls
# C for clear
from turtle import Turtle, Screen
import random as r
import time

colors = ["red", "orange", "yellow", "green", "blue", "purple"]


def create_turtle_color(t_color):
    """
    Provide a color and a turtle is created with that color and with its pen up
    """
    t = Turtle("turtle")
    t.color(t_color)
    t.penup()
    return t


screen = Screen()
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, startx=0, starty=0)
user_bet = screen.textinput(title="Make your bet", prompt="Bet on a turtle! What color are you betting on?")

NUMBER_OF_TURTLES = len(colors)
TURTLE_Y_SIZE = 10
TURTLE_Y_SEPARATION = 15
TURTLE_X_MARGIN = -SCREEN_WIDTH // 2 + TURTLE_Y_SIZE
TURTLE_Y_MARGIN = SCREEN_HEIGHT // 2 - NUMBER_OF_TURTLES * (TURTLE_Y_SIZE + TURTLE_Y_SEPARATION)  # Even spread

turtles = []

i = 0
for color in colors:
    turtle = create_turtle_color(color)
    turtle.goto(TURTLE_X_MARGIN, TURTLE_Y_MARGIN - i * (TURTLE_Y_SIZE + TURTLE_Y_SEPARATION))  # From top to bottom
    turtles.append(turtle)
    i += 1

winner = None
placement = []
times = []
start_time = time.time()
while len(placement) < NUMBER_OF_TURTLES:
    for turtle in turtles:
        turtle.forward(r.randint(1, 10))
        if turtle.xcor() > SCREEN_WIDTH // 2 and not turtle.pencolor() in placement:
            placement.append(turtle.pencolor())
            times.append(round(time.time()-start_time, 2))

if placement[0] == user_bet:
    print("You won the bet!")
else:
    print("You lose!")
print(f"The winner is: {placement[0]}")
print("\nLeaderboard:")

for index in range(0, NUMBER_OF_TURTLES):
    print(f"{index+1}. {placement[index]} - {times[index]}s")


screen.exitonclick()
