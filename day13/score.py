from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_score_board()

    def update_score_board(self):
        self.write(f"Score: {self.score}", align="center",
                   font=("Arial", 20, "bold"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.update_score_board()

    def game_over(self):
        self.goto(0, 0)
        self.clear()
        self.write(f"Game over your score: {self.score}", align="center",
                   font=("Arial", 20, "bold"))
