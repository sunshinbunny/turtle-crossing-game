FONT = ("Courier", 20, "normal")

from turtle import Turtle

class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.player_level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-280, 240)
        self.write(f"Level: {self.player_level}", align="left", font=FONT)

    def level_increase(self):
        self.player_level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="left", font=FONT)
