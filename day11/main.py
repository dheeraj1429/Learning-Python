import sys
import math
import random
from functools import reduce

# first = sys.argv[1]
# second = sys.argv[2]
# print(f'first: {first} second: {second}')


# def isPrime(num):
#     is_prime = False
#     if (num < 0):
#         return is_prime
#     if (num % 2 == 0):
#         return is_prime
#     for item in range(2, num):
#         if (num % item == 0):
#             is_prime = False
#     is_prime = True
#     return is_prime


# number = int(input("Please enter a number \n"))
# print(isPrime(number))


# alfa = ["a", "b", "c", "d", "e", "e", "f", "g", "h", "i", "j", "k", "l",
#         "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# shift_number_count = 2
# my_str = 'this'


# def shift_string(str, shift_count, type):
#     new_str = ''
#     for char in str:
#         char_index = 0
#         if (type == 'encode'):
#             char_index = alfa.index(char) + shift_count
#         else:
#             char_index = alfa.index(char) - shift_count
#         char = alfa[char_index]
#         new_str += char
#     return new_str


# encode = shift_string(my_str, shift_number_count, 'encode')
# decode = shift_string(encode, shift_number_count, 'decode')

# traval_log = [
#     {
#         "country": "France",
#         "visits": 12
#     },
#     {
#         "country": "Germany",
#         "visits": 5
#     }
# ]


# def add_new_traval(country_name, country_visits):
#     new_traval_log = traval_log[:]
#     new_traval_log.append(
#         {'country': country_name, 'visits': country_visits})
#     return new_traval_log


# new_traval = add_new_traval("United States", 4)


# auction_participants = []
# is_participant = True


# while (is_participant):
#     user_name = input("Enter your username\n")
#     auction_price = int(input("Enter your auction price\n"))
#     auction_participants.append(
#         {"auction_user": user_name, "auction_price": auction_price})

#     more_users = input(
#         "Are you sure you want to continue 'yes' or 'no'").lower()

#     first_auction_participant = auction_participants[0]

#     # find the max price of user.
#     for item in auction_participants:
#         if item['auction_price'] > first_auction_participant['auction_price']:
#             first_auction_participant = item

#     if (more_users == "no"):
#         is_participant = False
#         print(first_auction_participant)


# def leep_year(year):
#     """
#     Documention

#     @param year: This is the year
#     """
#     if (year % 4 == 0):
#         if (year % 100 == 0):
#             if (year % 400 == 0):
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# def add_function():
#     print('Adding')


# symbol_dict = {
#     "+": add_function
# }

# selected_symbol = "+"

# calculate_function = symbol_dict[selected_symbol]

# calculate_function()
# def genrate_two_random_numbers():
#     first = math.floor(random.random() * 10)
#     second = math.floor(random.random() * 10)

#     return [first, second]


# def sum(a, b):
#     return a + b


# def black_jack():
#     my_cards = []
#     computer_cards = []

#     # genrate random number
#     my_random_numbers = genrate_two_random_numbers()
#     computer_random_numbers = genrate_two_random_numbers()
#     my_cards = my_random_numbers
#     computer_cards = computer_random_numbers

#     my_number_sum = reduce(sum, my_cards)
#     computer_number_sum = reduce(sum, computer_cards)

#     print(f'You card numbers: {my_cards}')
#     print(f'Computer card numbers: {computer_cards}')

#     if (my_number_sum > computer_number_sum):
#         print("You win")
#     else:
#         print("Computer wins")


# black_jack()

# global scope
# is_valid = True

# if 2 < 3:
#     new_var = 'this is the new variable'
#     print(is_valid)

# print(new_var)

# function scope
# global_variable = 20


# def some_function():
# function scope
#     print(global_variable)
#     new_var = 'this is the new variable'


# some_function()
# print(new_var)


# modify global variable
# some_global_variable = 20


# def some_function():
#     global some_global_variable
#     some_global_variable = 30
#     print(some_global_variable)


# some_function()
# print(some_global_variable)

# lifes = 5
# is_playing = False


# def guess_number():
#     hidden_number = math.floor(random.random() * 100)
#     return hidden_number


# hidden_number = guess_number()


# def check_my_guessed_number():
#     global is_playing
#     global lifes

#     my_number = int(input("Guessing number "))

#     if (lifes <= 1):
#         is_playing = True
#         print(
#             f"guessing number is {hidden_number}, You lose, you dom ass hole!")

#     if (my_number == hidden_number):
#         print('Hooo your guessed number is correct')
#         is_playing = True
#     elif (my_number < hidden_number):
#         lifes -= 1
#         print(
#             f"Your guessed number is too low try again, you have only {lifes} lifes left")
#     elif (my_number < hidden_number):
#         lifes -= 1
#         print(
#             f"Your guessed number is too high try again, you have only {lifes} lifes left")


# while not is_playing:
#     check_my_guessed_number()


# guess_number()


# demo_data = [
#     {"name": "aman", "age": 20},
#     {"name": "Dheeraj", "age": 23},
#     {"name": "Roshan", "age": 19},
# ]
# index_count = 0
# score = 0
# game_play = False


# def guess_pro():
#     global index_count, score, game_play
#     next_count = index_count + 1

#     print(index_count)

#     check_from = demo_data[index_count]
#     check_to = demo_data[next_count]

#     print(f"is {check_from['name']} age is grater then {check_to['name']} age")
#     value = input("Please chose higher and lower ").lower()

#     if (value == 'higher'):
#         if (check_from["age"] > check_to['age']):
#             score += 1
#             index_count += 1
#             print('You are right')
#         else:
#             game_play = True
#             print("You are worng")
#     elif (value == "lower"):
#         if (check_from["age"] < check_to["age"]):
#             score += 1
#             index_count += 1
#             print('You are right')
#         else:
#             game_play = True
#             print("You are worng")
#     else:
#         print('You are wrong')
#         game_play = True

#     print(value)


# while not game_play:
#     guess_pro()
