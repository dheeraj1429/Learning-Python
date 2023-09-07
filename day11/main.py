import sys
import math

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
