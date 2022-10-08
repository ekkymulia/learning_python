import turtle
from turtle import Turtle, Screen
import random

t = Turtle()

turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)


t.shape("turtle")
t.pensize(10)
t.speed('fastest')

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
#             "SeaGreen"]


direction = [0, 90, 180, 270]

for _ in range(1000):
    t.pencolor(random_color())
    t.setheading(random.choice(direction))
    t.forward(30)

s = Screen()
s.exitonclick()