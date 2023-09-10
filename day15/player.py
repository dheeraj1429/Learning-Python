from turtle import Turtle
MOVE_SPEED = 20
INITAL_POSTION = (0, -270)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.shape('turtle')
        self.goto(INITAL_POSTION)
        self.setheading(90)

    def move(self):
        self.forward(MOVE_SPEED)

    def reset(self):
        self.goto(INITAL_POSTION)
