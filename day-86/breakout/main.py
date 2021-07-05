import random
from turtle import Screen
from paddle import Paddle
from game_world import Ball, Bricks, Border
import time
from scoreboard import Score
import numpy as np

SCREEN_SIZE = (800, 600)

screen = Screen()
paddle = Paddle()
ball = Ball()
score = Score()
ball.create()
screen.tracer(0)

x_pos_list = np.linspace(-400, 400, num=9)
x_pos_list = list(x_pos_list)

paddle.create(0, -350)


brick = Bricks()

for position in x_pos_list:
    brick.add_green(position)
    brick.add_yellow(position)
    brick.add_orange(position)
    brick.add_red(position)

border = Border()
border.create()

screen.bgcolor("black")
screen.screensize(SCREEN_SIZE[0], SCREEN_SIZE[1])

screen.title("Breakout")

screen.listen()

screen.onkey(paddle.right_side, "Right")
screen.onkey(paddle.left_side, "Left")

list_of_bricks = [brick.red_segments, brick.green_segments, brick.orange_segments, brick.yellow_segments]

game_is_on = True
time_sleep = 0.1
while game_is_on:

    screen.update()
    time.sleep(time_sleep)
    ball.move()
    if ball.ycor() > 360:
        ball.bounce_y()
    if ball.xcor() > 450 or ball.xcor() < -450:
        ball.bounce_x(change_direction=True)

    if paddle.distance(ball) < 40 and -335 > ball.ycor():
        ball.bounce_y()

    elif ball.ycor() < -360:
        time_sleep = 0.1
        ball.goto(0, -340)
        score.reduce_lives()
        change_directions = random.choice([True, False])
        ball.bounce_x(change_direction=change_directions)
        ball.bounce_y()

    for element in brick.green_segments:
        if ball.distance(element) < 45:
            element.reset()
            brick.green_segments.remove(element)
            ball.bounce_y()
            if time_sleep >= 0.1:
                time_sleep = 0.1
            score.increase_score(1)


    for element in brick.yellow_segments:
        if ball.distance(element) < 45:
            element.reset()
            brick.yellow_segments.remove(element)
            ball.bounce_y()
            if time_sleep >= 0.075:
                time_sleep = 0.075
            score.increase_score(2)


    for element in brick.orange_segments:
        if ball.distance(element) < 45:
            element.reset()
            brick.orange_segments.remove(element)
            ball.bounce_y()
            if time_sleep >= 0.05:
                time_sleep = 0.05
            score.increase_score(3)


    for element in brick.red_segments:
        if ball.distance(element) < 45:
            element.reset()
            brick.red_segments.remove(element)
            ball.bounce_y()
            if time_sleep >= 0.025:
                time_sleep = 0.025
            score.increase_score(4)


    if score.lives==0:
        score.update_scoreboard(ongoing=False, victory=False)
        game_is_on = False

    if all(len(a) == 0 for a in list_of_bricks):
        score.update_scoreboard(ongoing=False, victory=True)
        ame_is_on = False




screen.exitonclick()