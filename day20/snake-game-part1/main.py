import turtle as t
import time
from snake import Snake
from food import Food
from scores import ScoreBoard

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('orange')
screen.title("Snake Game")
screen.tracer(0)
game_running = True

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while True:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.scored()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset_pos()
        #break

    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            scoreboard.reset()
            snake.reset_pos()
            #break

    
        




screen.exitonclick()