import turtle
from turtle import Screen
import time

from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Screen Game')
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.right,'Right')
screen.onkey(snake.left,'Left')

game_is_on = True
while game_is_on :
    screen.update()  # Update only after moving all segments
    time.sleep(0.1)  # Slow down the loop for smoother movement
    snake.move_forward()

    if snake.head.distance(food)<15:
        food.refresh()
        score.increase_score()
        snake.add_turtle()
    if snake.head.xcor()>288 or snake.head.xcor()<-288 or snake.head.ycor()>288 or snake.head.ycor()<-288:
        game_is_on = False
        score.game_over()

screen.exitonclick()
