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


my_space_ship = turtle_gui.MyShip()

screen.onkey(my_space_ship.right_side, "Right")
screen.onkey(my_space_ship.left_side, "Left")

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

protect = turtle_gui.Protection()
protect.hideturtle()

for left, center, right in zip(left_pos, center_pos, right_pos):
    for y_pos in list(np.linspace(-50, -100, 3)):
        protect.add_left(left, y_pos)
        protect.add_center(center, y_pos)
        protect.add_right(right, y_pos)

protect.hideturtle()

## evils

evil = turtle_gui.Opponents()
evil.hideturtle()
positions = list(np.linspace(-300, 300, 10))
for pos in positions:
    for y_pos in list(np.linspace(270, 150, 3)):
        evil.evil_ship(pos, y_pos)

evil.hideturtle()

# move evils:
game_is_on = True

#def move_evil():


#weapon
my_fire = turtle_gui.Ammunition()

def start_a_fire():
    my_fire.my_weapon(my_space_ship.spaceship.xcor(), my_space_ship.spaceship.ycor(), 30)

# fire-test
screen.onkey(start_a_fire, 'Up')

while game_is_on:
    time.sleep(0.1)
    evil.check_direction()
    my_fire.move_weapon()
    my_fire.check_hit()

#if my_fire.defender[0].ycor() >= 300:
 #   my_fire.defender[0].reset()



screen.exitonclick()

