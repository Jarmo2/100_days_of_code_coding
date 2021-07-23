import time
from turtle import Turtle, Screen
import turtle_gui
import numpy as np


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
    for y_pos in list(np.linspace(270, 150, 3)):
        game.evil_ship(pos, y_pos)


# move evils:
game_is_on = True


def start_a_fire():
    game.my_weapon(game.spaceship.xcor(), game.spaceship.ycor(), 30)

# fire-test
screen.onkey(start_a_fire, 'Up')

while game_is_on:
    time.sleep(0.1)
    game.check_direction()
    game.move_weapon()
    game.check_hit()
    game.check_collision()
    game.evil_weapon()
    game.move_evil_weapon()

screen.exitonclick()

