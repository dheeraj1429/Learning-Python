# create_new_coffee = False
# ingredient = {
#     "watter": 300,
#     "milk": 200,
#     "coffe": 100,
#     "money": 0
# }

# products = [
#     {
#         "product_name": "espreesso",
#         "watter": 100,
#         "milk": 100,
#         "coffe": 40,
#     }, {
#         "product_name": "cappuccino",
#         "watter": 120,
#         "milk": 150,
#         "coffe": 80
#     }
# ]


# def get_product(product_name):
#     selected_product = {}
#     for product in products:
#         if (product["product_name"] == product_name):
#             selected_product = product
#     return selected_product


# def genrate_coffe():
#     global create_new_coffee
#     user_coffe_order = input(
#         "What do you want to ? (espreesso/cappuccino): ").lower()

#     if (user_coffe_order == "cappuccino" or user_coffe_order == "espreesso"):
#         selected_product = get_product(user_coffe_order)
#         print(selected_product)

#         if (selected_product and "product_name" in selected_product):
#             watter = selected_product["watter"]
#             milk = selected_product["milk"]
#             coffe = selected_product["coffe"]

#             if (ingredient["watter"] >= watter and ingredient["milk"] >= milk and ingredient["coffe"] >= coffe):
#                 ingredient["watter"] -= watter
#                 ingredient["milk"] -= milk
#                 ingredient["coffe"] -= coffe
#                 ingredient["money"] += 150

#                 print(
#                     f'here is your {selected_product["product_name"]} with ingredient, watter: {watter}, Watter: {milk}, Coffee: {coffe}')
#             else:
#                 print("OOPS! sorry we don't have enough ingridient")
#                 create_new_coffee = True
#         else:
#             print(
#                 "Oops! We don't have a product with that name, plase selected with ( espreesso/cappuccino )")

#         recreate = input("You want to create a new coffee, Y or N").lower()
#         if (recreate == 'n'):
#             create_new_coffee = True

#     else:
#         print("Please select between espreesso and cappuccino")


# while not create_new_coffee:
#     genrate_coffe()

# print(ingredient)
