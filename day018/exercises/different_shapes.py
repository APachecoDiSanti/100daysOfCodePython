from turtle import *
import random

screen = Screen()
screen.colormode(255)
turtle = Turtle()
turtle.shape("turtle")

for number_of_sides in range(3, 11):
    turtle.pencolor(
        (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
    )
    angle = 360/number_of_sides
    for _ in range(number_of_sides):
        turtle.forward(100)
        turtle.right(angle)

screen.exitonclick()
