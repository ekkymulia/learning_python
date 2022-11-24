import time
from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('pong')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()

screen.onkey(r_paddle.goUp, 'Up')
screen.onkey(r_paddle.goDown, 'Down')

screen.onkey(l_paddle.goUp, 'w')
screen.onkey(l_paddle.goDown, 's')


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.x_bounce()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    if ball.xcor() > 370:
        score.l_points()
        ball.restart()

    if ball.xcor() < -370:
        score.r_points()
        ball.restart()

screen.exitonclick()