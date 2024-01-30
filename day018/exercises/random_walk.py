from turtle import *
import random

screen = Screen()
screen.colormode(255)

turtle = Turtle()
turtle.shape("turtle")
turtle.pensize(10)
turtle.speed("fastest")

angles = [0, 90, 180, 270]

for _ in range(500):
    turtle.pencolor(
        (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
    )
    turtle.setheading(random.choice(angles))
    turtle.forward(30)

screen.exitonclick()
