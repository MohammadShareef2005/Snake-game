import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scorebord

scr = Screen()
scr.tracer(0)
Score = 0
scr = Screen()
fo = Food()
score_b = Scorebord()
scr.setup(height=600, width=600)
scr.bgcolor('black')
scr.title("Snake game ")

snake = Snake()
scr.listen()
scr.onkey(snake.up, 'Up')
scr.onkey(snake.down, 'Down')
scr.onkey(snake.left, 'Left')
scr.onkey(snake.right, 'Right')
game_on = True

while game_on:
    scr.update()
    time.sleep(0.3)
    snake.move()
    if snake.segments[0].distance(fo) < 15:
        fo.new_pos()
        snake.extend_b()
        score_b.inc()
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() < -280 or snake.segments[0].ycor() > 280:
        score_b.reset()
        snake.reset()

    for seg in snake.segments:
        if seg == snake.segments[0]:
            pass
        elif snake.segments[0].distance(seg) < 10:
            score_b.reset()
            snake.reset()
scr.exitonclick()
