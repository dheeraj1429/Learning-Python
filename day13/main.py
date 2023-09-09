
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
