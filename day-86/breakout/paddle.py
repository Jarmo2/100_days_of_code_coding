from turtle import Turtle

class Paddle(Turtle):

    def __init__(self):
        super().__init__()


    def create(self, go_to_x, go_to_y):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(go_to_x, go_to_y)


    def right_side(self):
        if self.xcor() < 450 or self.xcor() > -450:
            new_x = self.xcor() + 25
            self.goto(new_x, self.ycor())

    def left_side(self):
        if self.xcor() < 450 or self.xcor() > -450:
            new_x = self.xcor() - 25
            self.goto(new_x, self.ycor())