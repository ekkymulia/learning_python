import turtle
from turtle import Turtle, Screen
import random

t = Turtle()
t.shape("turtle")
t.speed('fastest')
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)

for _ in range(100):
    t.pencolor(random_color())
    t.circle(80)
    t.setheading(t.heading() + 10)


s = Screen()
s.exitonclick()