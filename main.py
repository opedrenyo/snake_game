from turtle import Screen
import time
from snake import Snake
from food import Food

GAME_IS_ON = True
screen = Screen()
screen.setup(width = 800, height = 800)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(key= "Up", fun = snake.up)
screen.onkey(key= "Down", fun = snake.down)
screen.onkey(key= "Right", fun = snake.right)
screen.onkey(key= "Left", fun = snake.left)


while GAME_IS_ON:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    

        

screen.exitonclick()