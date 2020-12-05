from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.pu()
        self.go_to_start()
        self.setheading(90)

    def up(self):
        self.fd(MOVE_DISTANCE)

    def down(self):
        self.bk(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(0, -280)

    def is_at_finish_line(self):
        if self.ycor() > 280:
            return True
        else:
            return False
