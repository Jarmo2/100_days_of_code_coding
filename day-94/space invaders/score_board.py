from turtle import Turtle
import config

ALIGNMENT = "center"
FONT = ("courier", 24, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.paddle_result = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 280)
        self.lives = 4
        self.update_scoreboard(ongoing=True, victory=False)

    def update_scoreboard(self, ongoing, victory):
        if ongoing:
            self.write(f"Player's score: {self.paddle_result} Remaining lives: {self.lives}", False, align=ALIGNMENT, font=FONT)
        if not ongoing:
            if victory:
                self.clear()
                self.write(f"Good job! You have won. This is your score: {self.paddle_result}", False, align=ALIGNMENT, font=FONT)
                config.game_is_on = False
                return config.game_is_on
            else:
                self.clear()
                self.write(f"That's it. Your result is: {self.paddle_result}", False, align=ALIGNMENT, font=FONT)
                config.game_is_on = False
                return config.game_is_on


    def increase_score(self, increase):
        self.paddle_result += increase
        self.clear()
        self.update_scoreboard(ongoing=True, victory=False)


    def reduce_lives(self, live):
        self.lives -= live
        self.clear()
        if self.lives == 0:
            self.update_scoreboard(ongoing=False, victory=False)
        else:
            self.update_scoreboard(ongoing=True, victory=False)