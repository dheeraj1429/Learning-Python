from turtle import Screen
from player import Player
from car import Car
from score import Score
import time


game_on = True
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = Car()
score = Score()

# listen events
screen.listen()
screen.onkey(key="w", fun=player.move)


while game_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_car()

    for op in car.all_cars:
        if (op.distance(player) < 22):
            game_on = False

    if (player.ycor() == 270):
        player.reset()
        car.speed_up()
        score.update_score()
        score.show_score()


screen.exitonclick()
