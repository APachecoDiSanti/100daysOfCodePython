from turtle import *

turtle = Turtle()
turtle.shape("turtle")

for _ in range(15):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()

screen = Screen()
screen.exitonclick()
