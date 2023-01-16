from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width = 800, height = 800)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)

snake = Snake()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    

        

screen.exitonclick()