from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="Left", font=("ComicSans", 20, "normal"))

    def level_up_scoreboard(self):
        self.level += 1
        self.update_scoreboard()

    def screen_game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="Left", font=("ComicSans", 20, "normal"))
