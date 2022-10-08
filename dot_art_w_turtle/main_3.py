from turtle import Turtle, Screen
import random

tim = Turtle()

tim.shape("turtle")

colours = ['black', 'yellow', 'red', 'green', 'blue', 'pink', 'aquamarine', "chartreuse"]


def draw_shape(num_side):
    angle = 360 / num_side
    for _ in range(num_side):
        tim.forward(100)
        tim.right(angle)


for n in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(n)


screen = Screen()
screen.exitonclick()