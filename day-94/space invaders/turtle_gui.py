import random
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

    def add_left_barrier(self, x_pos, y_pos):
        new_element = turtle.Turtle()
        new_element.shape('square')
        new_element.shapesize(stretch_wid=1, stretch_len=1)
        new_element.penup()
        new_element.goto(x_pos, y_pos)
        self.all_barriers.append(new_element)


    def add_right_barrier(self, x_pos, y_pos):
        new_element = turtle.Turtle()
        new_element.shape('square')
        new_element.shapesize(stretch_wid=1, stretch_len=1)
        new_element.penup()
        new_element.goto(x_pos, y_pos)
        self.all_barriers.append(new_element)


    def add_center_barrier(self, x_pos, y_pos):
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
            if ship.ycor() < 400:
                ship.goto(int(ship.xcor()+self.move_direction), ship.ycor())

    def evil_weapon(self):
        can_fire = []
        for opponent in self.opponents:
            if opponent.ycor() < 400:
                can_fire.append(opponent)
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
        increase_score = 0
        for opponent in self.opponents:
            for my_fire in self.defender_weapon:
                if my_fire.ycor() == opponent.ycor() and abs(my_fire.xcor()-opponent.xcor()) <=10:
                    opponent.goto(opponent.xcor(), 400)
                    my_fire.goto(my_fire.xcor(), 400)
                    increase_score = 1
        return increase_score

    def check_collision(self):
        for barrier in self.all_barriers:
            for my_fire in self.defender_weapon:
                if my_fire.ycor() == barrier.ycor() and abs(barrier.xcor()-my_fire.xcor()) <=10:
                    barrier.goto(barrier.xcor(), 500)
                    my_fire.goto(barrier.xcor(), 300)


    def check_collision_evil(self):
        for barrier in self.all_barriers:
            for evil_fire in self.attacker_weapon:
                if evil_fire.ycor() == barrier.ycor() and abs(barrier.xcor()-evil_fire.xcor()) <= 10:
                    barrier.goto(barrier.xcor(), 500)
                    evil_fire.goto(evil_fire.xcor(), -300)


    def hit_by_evil(self):
        reduce_live = 0
        for evil_fire in self.attacker_weapon:
            if evil_fire.ycor() == self.spaceship.ycor() and abs(evil_fire.xcor()-self.spaceship.xcor()) <= 10:
                reduce_live = 1
                evil_fire.ht()
                del evil_fire
        return reduce_live


    def check_out_of_game(self):
        for weapon in self.defender_weapon:
            if weapon.ycor() > 300:
                weapon.ht()
                del weapon
        for weapon in self.attacker_weapon:
            if weapon.ycor() < -300:
                weapon.ht()
                del weapon

    def weapons_collide(self):
        for my_weapon in self.defender_weapon:
            for evil_weapon in self.attacker_weapon:
                    if evil_weapon.ycor() == my_weapon.ycor() and abs(evil_weapon.xcor()-my_weapon.xcor()) <=15:
                        evil_weapon.goto(evil_weapon.xcor(), -330), my_weapon.goto(my_weapon.xcor(), 330)


    def ship_to_right_side(self):
        if self.spaceship.xcor() < 330 or self.spaceship.xcor() > -330:
                new_x = self.spaceship.xcor() + 20
                self.spaceship.goto(new_x, self.spaceship.ycor())


    def ship_to_left_side(self):
        if self.spaceship.xcor() < 330 or self.spaceship.xcor() > -330:
            new_x = self.spaceship.xcor() - 20
            self.spaceship.goto(new_x, self.spaceship.ycor())


    def check_the_end(self):
        list_of_targets = []
        for opponent in self.opponents:
            if opponent.ycor() < 330:
                list_of_targets.append(opponent)
        if len(list_of_targets) == 0:
            ongoing = False
            victory = True
            return ongoing, victory
        ongoing = True
        victory = False
        return ongoing, victory


