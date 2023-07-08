import turtle as t
from player import Player
from ball import Ball
import time

screen = t.Screen()
screen.title("PONG")
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)

paddle_1 = Player((350, 0))
paddle_2 = Player((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(paddle_1.go_up, "Up")
screen.onkey(paddle_1.go_down, "Down")
screen.onkey(paddle_2.go_up, 'w')
screen.onkey(paddle_2.go_down, 's')

while True:
    time.sleep(0.05)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(paddle_1) < 50 and ball.xcor() > 320 or ball.distance(paddle_2) < 50 and ball.xcor() < -320:
        ball.catch()

screen.exitonclick()