from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from field import Field

game_is_on = True

screen = Screen()
screen.title("Pong game")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))
ball = Ball()
field = Field()

field.center_circle()
field.center_divider()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


while game_is_on:
    screen.update()
    time.sleep(.06)
    ball.move()

    if (ball.ycor() > 300 or ball.ycor() < -300):
        ball.bounce_y()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -350):
        ball.bounce_x()

    if (ball.xcor() > 400 or ball.xcor() < -400):
        game_is_on = False


screen.exitonclick()
