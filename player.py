from turtle import Turtle

STARTING_POSITION = (0, -285)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 288

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.start_again()
        self.setheading(90)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def start_again(self):
        self.goto(STARTING_POSITION)
