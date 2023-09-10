from turtle import Turtle


class Field(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def center_circle(self):
        self.goto(0, -100)
        self.color("green")
        self.pendown()
        self.circle(100)

    def center_divider(self):
        self.penup()
        self.goto(0, 400)
        self.pendown()
        self.color("green")
        self.goto(0, -400)
