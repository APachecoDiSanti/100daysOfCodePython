import turtle as t
import random


def random_color():
    """
    Return a random tuple representing a color as in (r, g, b)
    """
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


screen = t.Screen()
screen.colormode(255)

turtle = t.Turtle()
turtle.shape("turtle")
turtle.pensize(2)
turtle.speed("fastest")

start_angle = 0
angle_step = 6

# Draw a number of circles of 100 radius

for _ in range(360 // angle_step):
    turtle.pencolor(random_color())
    turtle.setheading(turtle.heading() + angle_step)
    turtle.circle(100)

screen.exitonclick()
