from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

GAME_IS_ON = True
NEGATIVE_BORDER = -395
POSITIVE_BORDER = 395
snake_speed = 0.08

screen = Screen()
screen.setup(width = 800, height = 790)
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
    time.sleep(snake_speed)
    snake.move()
    
    
#DETECT COLLISION WITH FOOD
    if snake.head.distance(food) < 20:
        food.eaten()
        snake.eats()
        score.increase()
        snake_speed *= 0.9 
    
    if snake.head.xcor() < NEGATIVE_BORDER or snake.head.xcor() > POSITIVE_BORDER or snake.head.ycor() < NEGATIVE_BORDER or snake.head.ycor() > POSITIVE_BORDER:
        score.reset()
        snake.reset()

    if snake.collision():
        score.reset()
        snake.reset()


screen.exitonclick()