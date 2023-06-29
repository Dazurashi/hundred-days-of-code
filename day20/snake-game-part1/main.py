import turtle as t
import time
from snake import Snake

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('orange')
screen.title("Snake Game")
screen.tracer(0)
game_running = True

snake = Snake()



while True:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
        




screen.exitonclick()