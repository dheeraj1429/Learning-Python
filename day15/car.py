from turtle import Turtle
import random

MOVE_INCREMENT = 10
COLORS = ["red", "green", "yellow", "blue", "purple", "orange", "orange"]


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.STARTING_MOVE_DISTENCE = 5

    def create_car(self):
        random_choise = random.randint(1, 6)
        if (random_choise == 1):
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-230, 230)
            new_car.setheading(180)
            new_car.goto(320, random_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.forward(self.STARTING_MOVE_DISTENCE)

    def speed_up(self):
        self.STARTING_MOVE_DISTENCE += MOVE_INCREMENT
