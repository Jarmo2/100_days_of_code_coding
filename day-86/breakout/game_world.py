from turtle import Turtle

class Border(Turtle):

    def create(self):
        self.half_width = -470
        self.half_height = -380

        self.color("white")
        self.penup()
        self.goto(self.half_width, self.half_height)
        self.pendown()
        self.pensize(20)
        self.forward(self.half_width*-2)  # Forward turtle by s units
        self.left(90)  # Turn turtle by 90 degree
        self.forward(self.half_height*-2)
        self.left(90)
        self.forward(self.half_width*-2)
        self.left(90)
        self.forward(self.half_height*-2)

class Ball(Turtle):

    def create(self):
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(0, -340)
        self.y_move = 10
        self.x_move = 10

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def bounce_x(self, change_direction):
        if change_direction:
            self.x_move *= -1
        else:
            self.x_move *= 1

    def bounce_y(self):
        self.y_move *= -1



class Bricks(Turtle):

    def __init__(self):
        self.green_segments = []
        self.yellow_segments = []
        self.orange_segments = []
        self.red_segments = []

    def add_green(self, x_pos):
        new_element = Turtle(shape="square")
        new_element.color("green")
        new_element.shapesize(stretch_wid=2, stretch_len=4)
        new_element.penup()
        new_element.goto(x_pos, -50)
        self.green_segments.append(new_element)

    def add_yellow(self, x_pos):
        new_element = Turtle(shape="square")
        new_element.color("yellow")
        new_element.shapesize(stretch_wid=2, stretch_len=4)
        new_element.penup()
        new_element.goto(x_pos, 50)
        self.yellow_segments.append(new_element)


    def add_orange(self, x_pos):
        new_element = Turtle(shape="square")
        new_element.color("orange")
        new_element.shapesize(stretch_wid=2, stretch_len=4)
        new_element.penup()
        new_element.goto(x_pos, 150)
        self.orange_segments.append(new_element)

    def add_red(self, x_pos):
        new_element = Turtle(shape="square")
        new_element.color("red")
        new_element.shapesize(stretch_wid=2, stretch_len=4)
        new_element.penup()
        new_element.goto(x_pos, 150)
        self.red_segments.append(new_element)
