from turtle import Turtle, Screen
import pandas

screen = Screen()
turtle = Turtle()

screen.title('U.S State Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

# is_game_on = True
correct_answer = []

# while is_game_on:

while len(correct_answer) < 50:
    score = len(correct_answer) | 0
    answer_state = screen.textinput(title=f'{score} answer true, Guess the state', prompt='What is the states name?').title()

    data = pandas.read_csv('50_states.csv')

    searched_data = data[data['state'] == answer_state]

    if answer_state == 'Exit':
        missing_state = [row for row in data['state'] if row not in correct_answer]

        printed = pandas.DataFrame(missing_state)
        printed.to_csv('to Learn Printed.csv')
        break

    if(len(searched_data) > 0):
        correct_answer.append(searched_data.state.item())

        turtle = Turtle()
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(int(searched_data.x), int(searched_data.y))
        turtle.write(searched_data.state.item())







