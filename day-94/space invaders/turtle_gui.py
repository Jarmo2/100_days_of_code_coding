import random
import time
import turtle


class Game(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.all_barriers = []
        self.opponents = []
        self.move_direction = 1
        self.defender_weapon = []
        self.spaceship = turtle.Turtle()
        self.spaceship.shape('turtle')
        self.spaceship.penup()
        self.spaceship.setposition(0, -250)
        self.spaceship.setheading(90)
        self.attacker_weapon = []

    def add_left_barrier(self, x_pos, y_pos=50):
        new_element = turtle.Turtle()
        new_element.shape('square')
        new_element.shapesize(stretch_wid=1, stretch_len=1)
        new_element.penup()
        new_element.goto(x_pos, y_pos)
        self.all_barriers.append(new_element)

    def add_right_barrier(self, x_pos, y_pos=50):
        new_element = turtle.Turtle()
        new_element.shape('square')
        new_element.shapesize(stretch_wid=1, stretch_len=1)
        new_element.penup()
        new_element.goto(x_pos, y_pos)
        self.all_barriers.append(new_element)

    def add_center_barrier(self, x_pos, y_pos=50):
        new_element = turtle.Turtle()
        new_element.shape('square')
        new_element.shapesize(stretch_wid=1, stretch_len=1)
        new_element.penup()
        new_element.goto(x_pos, y_pos)
        self.all_barriers.append(new_element)

    def evil_ship(self, x_pos, y_pos):
        new_element = turtle.Turtle()
        new_element.shape('triangle')
        new_element.shapesize(stretch_wid=1, stretch_len=2)
        new_element.setheading(-90)
        new_element.penup()
        new_element.goto(x_pos, y_pos)
        self.opponents.append(new_element)

    def check_direction(self):
        list_of_pos = []
        for ship in self.opponents:
            ship_loc = ship.xcor()
            list_of_pos.append(ship_loc)
        if 330 > int(max(list_of_pos, default=0)) and int(min(list_of_pos, default=0)) > -330:
            self.move_direction *= 1
        else:
            self.move_direction *= -1
        self.move_evil()

    def move_evil(self):
        for ship in self.opponents:
            ship.goto(int(ship.xcor()+self.move_direction), ship.ycor())

    def evil_weapon(self):
        list_of_y = []
        can_fire = []
        for evil in self.opponents:
            new_ycor = evil.ycor()-60
            list_of_y.append(evil.ycor())
            if new_ycor not in list_of_y:
                can_fire.append(evil)
        print(len(can_fire))
        print(len(self.opponents))
        firing = random.choice(can_fire)
        new_evil_fire = turtle.Turtle()
        new_evil_fire.shape('arrow')
        new_evil_fire.shapesize(stretch_wid=0.5, stretch_len=0.5)
        new_evil_fire.setheading(270)
        new_evil_fire.penup()
        new_evil_fire.setposition(firing.xcor(), firing.ycor())
        self.attacker_weapon.append(new_evil_fire)


    def move_evil_weapon(self):
        for weapon in self.attacker_weapon:
            weapon.setposition(weapon.xcor(), weapon.ycor()-10)

    def my_weapon(self, x_pos, y_pos, speed=15):
        new_weapon = turtle.Turtle()
        new_weapon.shape('arrow')
        new_weapon.shapesize(stretch_wid=0.5, stretch_len=0.5)
        new_weapon.setheading(90)
        new_weapon.penup()
        new_weapon.setposition(x_pos, y_pos)
        self.defender_weapon.append(new_weapon)

    def move_weapon(self):
        for weapon in self.defender_weapon:
            weapon.setposition(weapon.xcor(), weapon.ycor()+10)

    def check_hit(self):
        for opponent in self.opponents:
            for my_fire in self.defender_weapon:
                if my_fire.ycor() == opponent.ycor():
                    opponent.reset()
    ##check out of zone

    def check_collision(self):
        for barrier in self.all_barriers:
            for my_fire in self.defender_weapon:
                if my_fire.ycor() == barrier.ycor() and abs(barrier.xcor()-my_fire.xcor()) <=10:
                    barrier.reset()


    def ship_to_right_side(self):
        if self.spaceship.xcor() < 330 or self.spaceship.xcor() > -330:
                new_x = self.spaceship.xcor() + 20
                self.spaceship.goto(new_x, self.spaceship.ycor())
#
    def ship_to_left_side(self):
        if self.spaceship.xcor() < 330 or self.spaceship.xcor() > -330:
            new_x = self.spaceship.xcor() - 20
            self.spaceship.goto(new_x, self.spaceship.ycor())





