from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

GAME_IS_ON = True
screen = Screen()
screen.setup(width = 800, height = 800)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(key= "Up", fun = snake.up)
screen.onkey(key= "Down", fun = snake.down)
screen.onkey(key= "Right", fun = snake.right)
screen.onkey(key= "Left", fun = snake.left)


while GAME_IS_ON:
    screen.update()
    time.sleep(0.09)
    snake.move()
    
    
#DETECT COLLISION WITH FOOD
    if snake.head.distance(food) < 20:
        food.eaten_food()
        snake.snake_eats_food()
        score.increase_score()



        

screen.exitonclick()