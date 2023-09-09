# from turtle import Turtle, Screen
# import time
# from snake import Snake
# from food import Food
# from score import Score

# import random

# class Restaurant:
#     _create_new_coffee = False
#     _ingredient = {
#         "watter": 300,
#         "milk": 200,
#         "coffe": 100,
#         "money": 0
#     }
#     _products = [
#         {
#             "product_name": "espreesso",
#             "watter": 100,
#             "milk": 100,
#             "coffe": 40,
#         }, {
#             "product_name": "cappuccino",
#             "watter": 120,
#             "milk": 150,
#             "coffe": 80
#         }
#     ]

#     def get_product(self, product_name):
#         selected_product = {}
#         for product in self._products:
#             if (product["product_name"] == product_name):
#                 selected_product = product
#         return selected_product

#     def genrate_coffe(self):
#         user_coffe_order = input(
#             "What do you want to ? (espreesso/cappuccino): ").lower()

#         if (user_coffe_order == "cappuccino" or user_coffe_order == "espreesso"):
#             selected_product = self.get_product(user_coffe_order)
#             print(selected_product)

#             if (selected_product and "product_name" in selected_product):
#                 watter = selected_product["watter"]
#                 milk = selected_product["milk"]
#                 coffe = selected_product["coffe"]

#                 if (self._ingredient["watter"] >= watter and self._ingredient["milk"] >= milk and self._ingredient["coffe"] >= coffe):
#                     self._ingredient["watter"] -= watter
#                     self._ingredient["milk"] -= milk
#                     self._ingredient["coffe"] -= coffe
#                     self._ingredient["money"] += 150

#                     print(
#                         f'here is your {selected_product["product_name"]} with ingredient, watter: {watter}, Watter: {milk}, Coffee: {coffe}')
#                 else:
#                     print("OOPS! sorry we don't have enough ingridient")
#                     self._create_new_coffee = True
#             else:
#                 print(
#                     "Oops! We don't have a product with that name, plase selected with ( espreesso/cappuccino )")

#             recreate = input("You want to create a new coffee, Y or N").lower()
#             if (recreate == 'n'):
#                 self._create_new_coffee = True

#         else:
#             print("Please select between espreesso and cappuccino")

#     def buy_coffee(self):
#         while not self._create_new_coffee:
#             self.genrate_coffe()


# new_restorent = Restaurant()

# print(new_restorent._products)
# new_restorent.buy_coffee()

# t = turtle.Turtle('turtle')
# t.shape("arrow")

# for _ in range(4):
#     t.forward(100)
#     t.right(90)

# turtle.done()


# t = turtle.Turtle('turtle')

# t.width(1)


# def draw_shape(num_slide):
#     angle = 360 / num_slide
#     t.color("red")
#     for _ in range(num_slide):
#         t.forward(100)
#         t.right(angle)


# for item in range(3, 11):
#     draw_shape(item)


# turtle.done()


# def draw_shape(num_slide):
#     angle = random.random() * 100
#     t.color("red")
#     for _ in range(num_slide):
#         t.forward(20)
#         t.right(angle)


# for item in range(100):
#     draw_shape(item)


# turtle.done()


# the tuple is a immutable list
# my_tuple = (1, 2, 3)
# my_tuple[1] = 10

# now we can change the values of the list.
# my_list = list(my_tuple)
# my_list[0] = 10
# print(my_list)

# we can change the values from the list.
# my_list = [1, 2, 3]
# my_list[1] = 10
# print(my_list)


# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color


# t.width(1)
# t.speed('fastest')


# def draw_shape():
#     current_heading = t.heading()
#     t.circle(100)
#     t.setheading(current_heading - 10)
#     t.circle(100)


# for _ in range(int(360 / 5)):
#     draw_shape()

# turtle.done()


# snake = Turtle()
# screen = Screen()

# screen.setup(width=600, height=600)
# screen.title("My snake game with python")


# def move_right():
#     snake.right(10)


# def move_left():
#     snake.left(10)


# def move_forward():
#     snake.forward(10)


# def move_backward():
#     snake.backward(10)


# def clear():
#     snake.clear()
#     snake.penup()
#     snake.home()
#     snake.pendown()


# screen.listen()
# screen.onkey(key='w', fun=move_forward)
# screen.onkey(key="a", fun=move_left)
# screen.onkey(key="d", fun=move_right)
# screen.onkey(key='s', fun=move_backward)
# screen.onkey(key="space", fun=clear)

# screen.exitonclick()

# screen = Screen()

# screen.setup(width=500, height=400)
# screen.title("Tummy race")
# colors = ["red", "green", "blue", "yellow", "black", "purple"]
# y_position = [-70, -40, -10, 20, 50, 80]
# is_race_on = False
# all_turtle = []
# winner_turtle = ''

# my_player = screen.textinput(
#     title="Place your bet", prompt="Which turtle will win the race? Enter a color: ")

# for turtle_index in range(0, 6):
#     new_turtle = Turtle()
#     new_turtle.penup()
#     new_turtle.shape('turtle')
#     new_turtle.goto(x=-230, y=y_position[turtle_index])
#     new_turtle.color(colors[turtle_index])
#     all_turtle.append(new_turtle)

# if my_player:
#     is_race_on = True

# while is_race_on:
#     for turtle in all_turtle:
#         turtle_speed = int(random.randint(0, 18))
#         turtle.forward(turtle_speed)
#         x_position = turtle.pos()[0]
#         if (x_position >= 230):
#             winner_turtle = turtle.color()[0]
#             is_race_on = False

# if (winner_turtle == my_player):
#     print("Hooowooo you win!")
# else:
#     print(f"You lose, Winner turtle: {winner_turtle}")

# screen.exitonclick()


# --------------------------------
# screen = Screen()
# screen.setup(width=600, height=600)
# game_on = True
# screen.tracer(0)

# snake = Snake()
# food = Food()
# score = Score()
# screen.title("My snake game")


# snake.create_snake()


# screen.listen()
# screen.onkey(key='w', fun=snake.up)
# screen.onkey(key='s', fun=snake.down)
# screen.onkey(key='d', fun=snake.left)
# screen.onkey(key='a', fun=snake.right)


# while game_on:
#     screen.update()
#     time.sleep(.1)

#     snake.move()

#     if (snake.get_head().distance(food) < 15):
#         food.refresh()
#         score.update_score()
#         snake.extend()

#     if (snake.get_head().xcor() > 280 or snake.get_head().xcor() < -280 or
#             snake.get_head().ycor() > 280 or snake.get_head().ycor() < -280):
#         game_on = False
#         score.game_over()


# screen.exitonclick()

# ----------------------------------------------------------------
# class Animal():
#     def __init__(self):
#         self.num_eyes = 2

#     def breath(self):
#         print("Inhal, exhale.")


# class Fish(Animal):
#     def __init__(self):
#         super().__init__()


# fish = Fish()
# print(fish.breath())
