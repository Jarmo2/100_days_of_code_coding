import time
from turtle import Turtle, Screen
import turtle_gui
import numpy as np
import score_board
import config


score = score_board.ScoreBoard()

#screen
screen = Screen()
screen.bgcolor('orange')
screen.title("Space Invaders")
screen.listen()
screen.tracer(2)


game = turtle_gui.Game()

screen.onkey(game.ship_to_right_side, "Right")
screen.onkey(game.ship_to_left_side, "Left")

## turtle = horizontal line

horizontal = Turtle()
horizontal.penup()
horizontal.setposition(-330, -270)
horizontal.pencolor('blue')
horizontal.pendown()
horizontal.setposition(330, -270)
horizontal.hideturtle()


## protection
left_pos = list(np.linspace(-300, -150, 4))
center_pos = list(np.linspace(-100, 100, 4))
right_pos = list(np.linspace(150, 300, 4))


for left, center, right in zip(left_pos, center_pos, right_pos):
    for y_pos in list(np.linspace(-50, -100, 3)):
        game.add_left_barrier(left, y_pos)
        game.add_center_barrier(center, y_pos)
        game.add_right_barrier(right, y_pos)


## evils

positions = list(np.linspace(-300, 300, 10))
for pos in positions:
    for y_pos in list(np.linspace(270, 150, 4)):
        game.evil_ship(pos, y_pos)


# move evils:
game_is_on = True


def start_a_fire():
    game.my_weapon(game.spaceship.xcor(), game.spaceship.ycor(), 30)

def opponent_fire():
    before = time.perf_counter()
    if before %3 <= 1:
        game.evil_weapon()


# fire-test
screen.onkey(start_a_fire, 'Up')


while config.game_is_on:
    time.sleep(0.001)
    score.reduce_lives(game.hit_by_evil())
    game.check_out_of_game()
    game.weapons_collide()
    game.check_direction()
    game.move_weapon()
    score.increase_score(int(game.check_hit()))
    game.check_collision()
    game.check_collision_evil()
    game.move_evil_weapon()
    opponent_fire()
    end = game.check_the_end()
    score.update_scoreboard(ongoing=end[0], victory=end[1])


screen.exitonclick()

