# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('damien-hirst-severed-spots-full-169.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle
import random

turtle.colormode(255)
turtl = turtle.Turtle()
turtl.speed('fastest')
turtl.penup()
turtl.hideturtle()
color_list = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252), (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40)]

turtl.setheading(225)
turtl.forward(300)
turtl.setheading(0)

number_of_dot = 100

for dot_count in range(1, number_of_dot + 1):
    turtl.dot(20, random.choice(color_list))
    turtl.forward(50)

    if dot_count % 10 == 0:
        turtl.setheading(90)
        turtl.forward(50)
        turtl.setheading(180)
        turtl.forward(500)
        turtl.setheading(0)

screen = turtle.Screen()
screen.exitonclick()
