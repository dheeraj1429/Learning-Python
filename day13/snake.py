from turtle import Turtle


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.starting_segments = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        self.move_distance = 20

    def get_head(self):
        return self.segments[0]

    def create_snake(self):
        """Create a snake"""
        for postion in self.starting_segments:
            new_segment = Turtle(shape='square')
            new_segment.penup()
            new_segment.goto(x=postion[0], y=postion[1])
            self.segments.append(new_segment)

    def add_segment(self, postion):
        new_segment = Turtle(shape='square')
        new_segment.penup()
        new_segment.goto(postion)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Move the snake"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(self.move_distance)

    def up(self):
        self.segments[0].setheading(90)

    def down(self):
        self.segments[0].setheading(270)

    def right(self):
        self.segments[0].setheading(180)

    def left(self):
        self.segments[0].setheading(0)
