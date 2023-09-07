# import random
# from utility import add
import utility

# import utility
# from time import time

# Error handling
# def sum_num(num):
#     return 5 / num


# sum_num(0)

# try:
#     age = int(input('what is your age?\n'))
#     print(age)
# except (ValueError, ZeroDivisionError) as err:
#     print(f'something worng: {err}')
# else:
#     print('done')
#     pass
# finally:
#     print('this will run every time you execute this script')

# try:
#     age = int(input('what is your age?\n'))
#     if (age == 10):
#         print(f'your age is {age}')
#     else:
#         raise ValueError('your age must be 10')
# finally:
#     pass

# Genrator
# def genrator_func(num):
#     for i in range(num):
#         yield i*2


# g = genrator_func(10)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# def performance(func):
#     def wrapped_func(*args, **kwargs):
#         t1 = time()
#         func(*args, **kwargs)
#         t2 = time()
#         print(f' took {t2 - t1} seconds')
#     return wrapped_func


# @performance
# def log_func():
#     print('1')
#     for item in range(100000000):
#         item * 5


# @performance
# def log_func_2():
#     print('2')
#     for item in list(range(100000000)):
#         item * 5


# log_func()
# log_func_2()

# class MyGen():
#     current = 0

#     def __init__(self, start, end):
#         self.start = start
#         self.end = end

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if MyGen.current < self.end:
#             num = MyGen.current
#             MyGen.current += 1
#             return num
#         raise StopIteration


# gen = MyGen(0, 10)
# for item in gen:
#     print(item)

# def fib(number):
#     a = 0
#     b = 1
#     for _ in range(number):
#         yield a
#         temp = a
#         a = b
#         b = temp + b


# for item in fib(10):
#     print(item)

# print('Welcome to the love calculator')
# name = input('What is your name\n')
# love_name = input('What is your partner name\n')


# def match_count(str):
#     sum = 0
#     for item in 'love':
#         sum += str.count(item)

#     return sum


# name_first = match_count(name.lower())
# name_second = match_count(love_name.lower())

# print(f'your love score if {name_first}{name_second}')
# road_path = input(
#     "You're at a cross road. where do you want to? Type 'left' or 'right'\n")
# if (road_path == 'right'):
#     print('You choose wrong direction. Game over')
# else:
#     print('some')

# random_integer = random.randint(1, 4)
# random_float = random.random() * 5
# print(random_float)

# names_string = input('Give me everybody name, seperated by a comma\n')
# names_list = names_string.split(', ')
# random_index = random.randint(0, len(names_list) - 1)
# print(names_list[random_index] + ' ' + 'is gooing to buy the meal today!')

# row1 = ['☐', '☐', '☐']
# row2 = ['☐', '☐', '☐']
# row3 = ['☐', '☐', '☐']

# map = [row1, row2, row3]

# place = int(input('Where do you wwant to put treasure?\n'))
# if place > 10:
#     place_in_str = str(place)
#     column = int(place_in_str[0]) - 1
#     row = int(place_in_str[1]) - 1
#     map[row][column] = 'x'
#     print(f"{row1}\n{row2}\n{row3}")
# else:
#     print('please enter two digits first one is a colume value and second one is row value')

# rock, paper, scissiors
# inital_list = ['rock', 'paper', 'scissiors']
# user_input = int(input(
#     'What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissiors\n'))
# computer_choice = random.randint(0, len(inital_list) - 1)

# print(
#     f'user choice: {inital_list[user_input]} and computer choice: {inital_list[computer_choice]}')

# average height of students
# student_height = [120, 203, 19, 30, 144]
# height_sum = 0
# for item in student_height:
#     height_sum += item

# average_height = round(height_sum / len(student_height))
# print(average_height)


# highest score in list
# student_scores = [78, 20, 10, 9, 10, 22]
# highest_score = student_scores[0]
# for item in student_scores:
#     if item > highest_score:
#         highest_score = item

# print(highest_score)

# for item in range(1, 100):
#     if (item % 3 == 0 and item % 5 == 0):
#         print('FizzBuzz')
#     elif (item % 3 == 0):
#         print('Fizz')
#     elif (item % 5 == 0):
#         print('Buzz')
#     else:
#         print(item)

# password genrator
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# symbols = ['!', '<', '>', '*', '%', ':', '=', '&']
# numbers = list(range(0, 10))
# print("welcome to the password genrator")
# nr_letters = int(input('How many letters do you want to?\n'))
# nr_symbols = int(input('How many symbols do you want to\n'))
# nr_numbers = int(input('How many numbers do you want to\n'))


# random_hash_list = []
# new_list = []


# def genrate_str(loop_count, li):
#     for _ in range(0, loop_count):
#         # if we want to get the random index then get the element based on the index.
#         # random_index = random.randint(0, len(li) - 1)
#         # hash += str(li[random_index])
#         random_hash_list.append(str(random.choice(li)))


# hash_letters = genrate_str(nr_letters, letters)
# hash_symbols = genrate_str(nr_symbols, symbols)
# hash_numbers = genrate_str(nr_numbers, numbers)
# random.shuffle(random_hash_list)
# hash = ''
# for i in random_hash_list:
#     hash += i
# print(f'Your hash password is: {hash}')


# guess letters
# words_list = ['book', 'nootbook', 'pen', 'data', 'code']
# random_word = words_list[random.randint(0, len(words_list) - 1)]
# blink_line = ''
# for i in random_word:
#     blink_line += '_'
# print(random_word)
# print(blink_line)

# guessed_words_list = ['_' for _ in random_word]

# life = len(words_list) - 1

# while life > 0:
#     # check user type letter is exsist in random words
#     user_letter = input('Guess the hide letters\n')
#     check_index = random_word.find(user_letter)
#     if (check_index == -1):
#         life -= 1
#         print(f'Oh no! only {life} life is left')
#     else:
#         guessed_words_list[check_index] = user_letter
#         blink_line = ''
#         for item in guessed_words_list:
#             blink_line += item
#         print(blink_line)

# print('Game over')

# word_list = ['ardvark', 'baboon', 'camal']
# chosen_word = random.choice(word_list)
# print(f'the solution is: {chosen_word}')

# display = ['_' for _ in chosen_word]
# end_of_game = False
# lifes = 6

# while not end_of_game:
#     guess = (input('Guess the word\n')).lower()
#     for position in range(len(chosen_word)):
#         letter = chosen_word[position]
#         if letter == guess:
#             display[position] = letter

#     print(display)

#     if guess not in chosen_word:
#         lifes -= 1
#         print(f'oh no you have only {lifes} life left')

#     if lifes <= 0:
#         print('Game over')
#         end_of_game = True

#     if '_' not in display:
#         end_of_game = True
#         print('You win')

# print(utility.add(1, 2))
# print(__name__)

