from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-10, 280)
        self.score = 0
        self.hideturtle()
        self.color("black")
        self.setheading(-90)
        self.show_score()

    def show_score(self):
        self.write(f"Score: {self.score}")

    def update_score(self):
        self.score += 1
        self.clear()
        self.show_score()
