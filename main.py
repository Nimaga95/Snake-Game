from turtle import Screen, Turtle
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

starting_position = [(0,0), (-20, 0), (-40, 0)]
segments = []
# Step 1 : Create the Snake Body : You can do it by many way
for position in starting_position:
    snake = Turtle(shape = "square")
    snake.color("white")
    snake.penup()
    snake.goto(position)
    segments.append(snake)

# Step 2 : Make move the Snake
screen.update()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(1)
    for element in segments:
        element.forward(20)








screen.exitonclick()