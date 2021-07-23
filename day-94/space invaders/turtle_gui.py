import turtle



class Protection(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.left = []
        self.center = []
        self.right = []

    def add_left(self, x_pos, y_pos=50):
        new_element = turtle.Turtle()
        new_element.shape('square')
        new_element.shapesize(stretch_wid=1, stretch_len=1)
        new_element.penup()
        new_element.goto(x_pos, y_pos)
        self.left.append(new_element)

    def add_right(self, x_pos, y_pos=50):
        new_element = turtle.Turtle()
        new_element.shape('square')
        new_element.shapesize(stretch_wid=1, stretch_len=1)
        new_element.penup()
        new_element.goto(x_pos, y_pos)
        self.right.append(new_element)

    def add_center(self, x_pos, y_pos=50):
        new_element = turtle.Turtle()
        new_element.shape('square')
        new_element.shapesize(stretch_wid=1, stretch_len=1)
        new_element.penup()
        new_element.goto(x_pos, y_pos)
        self.center.append(new_element)


class Opponents(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.opponents = []
        self.move_direction = 1

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
        if 330 > int(max(list_of_pos)) and int(min(list_of_pos)) > -330:
            self.move_direction *= 1
        else:
            self.move_direction *= -1
        self.move_evil()
        print('move function called')

    def move_evil(self):
        for ship in self.opponents:
            ship.goto(int(ship.xcor()+self.move_direction), ship.ycor())


class Ammunition(turtle.Turtle):


    def __init__(self):
        super().__init__()
        self.defender = []

    def my_weapon(self, x_pos, y_pos, speed=15):
        new_weapon = turtle.Turtle()
        new_weapon.shape('arrow')
        new_weapon.shapesize(stretch_wid=0.5, stretch_len=0.5)
        new_weapon.setheading(90)
        new_weapon.penup()
        new_weapon.setposition(x_pos, y_pos)
        self.defender.append(new_weapon)

    def move_weapon(self):
        for weapon in self.defender:
            weapon.setposition(weapon.xcor(), weapon.ycor()+10)

    def check_hit(self):
        for opponent in Opponents().opponents:
            for my_fire in self.defender:
                if my_fire.ycor() == opponent.ycor():
                    opponent.reset()


class MyShip(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.spaceship = turtle.Turtle()
        self.spaceship.shape('turtle')
        self.spaceship.penup()
        self.spaceship.setposition(0, -250)
        self.spaceship.setheading(90)

    def right_side(self):
        if self.spaceship.xcor() < 330 or self.spaceship.xcor() > -330:
                new_x = self.spaceship.xcor() + 20
                self.spaceship.goto(new_x, self.spaceship.ycor())

    def left_side(self):
        if self.spaceship.xcor() < 330 or self.spaceship.xcor() > -330:
            new_x = self.spaceship.xcor() - 20
            self.spaceship.goto(new_x, self.spaceship.ycor())





