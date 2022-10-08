from turtle import Turtle, Screen
import random

screen = Screen()

is_race_on = False

screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Place your bet!', prompt='Which color is the winner? Enter a color: ')

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_position = [-70, -40, -10, 20, 50, 80]

alL_turtle = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    new_turtle.color(colors[turtle_index])
    alL_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in alL_turtle:
        if(turtle.xcor() > 230):
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f'your {winning_color} turtle has won')
            else:
                print(f'You have lost, {winning_color} turtle has won instead')

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()