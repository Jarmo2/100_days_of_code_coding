from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 24, "normal")

class Score(Turtle):


    def __init__(self):
        super().__init__()
        self.paddle_result = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 280)
        self.lives = 3
        self.update_scoreboard(ongoing=True, victory=False)


    def update_scoreboard(self, ongoing, victory):
        if ongoing:
            self.write(f"Player's score: {self.paddle_result} Remaining lives: {self.lives}", False, align=ALIGNMENT, font=FONT)
        if not ongoing:
            if victory:
                self.clear()
                self.write(f"Good job! You have one. This is your score: {self.paddle_result}", False, align=ALIGNMENT, font=FONT)
            else:
                self.clear()
                self.write(f"That's it. Your result is: {self.paddle_result}", False, align=ALIGNMENT, font=FONT)


    def increase_score(self, increase):
        self.paddle_result += increase
        self.clear()
        self.update_scoreboard(ongoing=True, victory=False)


    def reduce_lives(self):
        self.lives -= 1
        self.clear()
        self.update_scoreboard(ongoing=True, victory=False)