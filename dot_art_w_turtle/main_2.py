from turtle import Turtle, Screen

tim = Turtle()

tim.shape('turtle')
# tim.color('chartreuse')


def dashed_line():
    tim.forward(5)
    tim.penup()
    tim.forward(10)
    tim.pendown()


for _ in range (10):
    for _ in range(5):
        dashed_line()

    tim.forward(45)
    tim.pendown()
    tim.forward(10)



screen = Screen()
screen.exitonclick()