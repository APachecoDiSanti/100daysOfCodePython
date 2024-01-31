import colorgram
import turtle as t
import random as r

# get list of tuples with the colors from the painting using colorgram
# colorgram_colors = colorgram.extract("painting.jpg", 100)
# colors = []
# for c in colorgram_colors:
#     rgb = c.rgb
#     rgb_tuple = (rgb.r, rgb.g, rgb.b)
#     colors.append(rgb_tuple)
# print(colors)

rgbs = [(211, 154, 98), (53, 107, 131), (177, 78, 33), (198, 142, 35), (116, 155, 171), (124, 79, 98), (123, 175, 157), (226, 197, 130), (190, 88, 109), (12, 50, 64), (56, 39, 19), (41, 168, 128), (50, 126, 121), (199, 123, 143), (166, 21, 30), (224, 93, 79), (243, 163, 161), (38, 32, 34), (3, 25, 25), (80, 147, 169), (161, 26, 22), (21, 78, 90), (234, 167, 171), (171, 206, 190), (103, 127, 156), (165, 202, 210), (61, 60, 72), (183, 190, 204), (78, 66, 42), (23, 99, 96)]


screen = t.Screen()

# Canvas Size 10x10, dots are 20 in size and separated by 50 paces
dots_per_line = 10
dot_diameter = 20
dot_center_separation = 50
canvas_padding = dot_diameter / 2

# half dot diameter from the left and from the right make 1 diameter to deduce
dot_center_difference = dot_center_separation - dot_diameter
# all the circles, plus the difference between them plus top and bottom or left and right padding
canvas_length = dot_diameter * dots_per_line + dot_center_difference * (dots_per_line - 1) + canvas_padding * 2
print(canvas_length)
print(dot_center_difference)
screen.setup(canvas_length, canvas_length, 0, 0)
screen.colormode(255)

turtle = t.Turtle()
turtle.shape("turtle")
turtle.penup()
turtle.speed("fastest")

furthest_away_from_center = -canvas_length / 2 + dot_diameter / 2 + canvas_padding
turtle.setx(furthest_away_from_center)
turtle.sety(furthest_away_from_center)

for _ in range(dots_per_line):
    for _ in range(dots_per_line):
        turtle.dot(dot_diameter, r.choice(rgbs))
        turtle.forward(dot_center_separation)
    turtle.left(90)
    turtle.forward(dot_center_separation)
    turtle.right(90)
    turtle.setx(furthest_away_from_center)

screen.exitonclick()
