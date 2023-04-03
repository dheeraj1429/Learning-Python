# data types
# print(len('hello'))
# print(len(12323)) type error

# string
# Iteger
# float
# boolean

# get the single char of the string from position 1
start = "hello"[1]
# print(start)

# get the last index of the string.
# print('hello'[-1])

# if we don't know what is the length of the string.
s = 'hello'
# print(s[len(s) - 1])

# Iteger
# print(123 + 456)
# print('123' + '456')

# large numbers
# print(123456789)
# print(123_456_789)

# Float
# print(1.123123)
# print(1.121)
# print(12.1123 + 1.123)

# boolean
# True
# False

# Number
# num_char = len(input('What is your name\n'))
# print('your name has' + num_char + 'char')  # return type error

# check the data type.
# print(type(num_char))

# type casting. type converstion where we can one pease of data type to the another data type
# like string to boolean or number to boolean ...
# num_char = len(input('What is your name\n'))
# print('your name has ' + str(num_char) + ' char')

a = str(10)
# print(type(a))

# -----------------------------------------
# string methods
# converts first character to uppercase and others to lowercase
# sentence = "i love PYTHON"
# capitalize_sentence = sentence.capitalize()
# print(capitalize_sentence)

# sentence = "i love PYTHON"
# first = sentence[0:1].upper()
# slice_first = sentence[1:len(sentence)].lower()
# print(first + slice_first)
# print(50 + float("100.2"))

# The center() method returns a new centered string after padding it with the specified character.
# c_str = 'password'
# new_string = c_str.center(15, '@')
# print(new_string)

# The casefold() method converts all characters of the string into lowercase letters and returns a new string.
# text = "pYtHon"
# new_string = text.casefold()
# print(new_string)

# The count() method returns the number of occurrences of a substring in the given string.
# string.count(substring, start=..., end=...)
# text = 'this is the best way to learn'
# c = text.count('t')
# print('Number of occurrence of ' + str(c))

# The endswith() method returns True if a string ends with the specified suffix. If not, it returns False
# string = 'this is me'
# isEnd = string.endswith('me')
# print(isEnd)

# text = "Python is easy to learn."
# result = text.endswith('to learn')
# # returns False
# print(result)

# result = text.endswith('to learn.')
# # returns True
# print(result)

# result = text.endswith('Python is easy to learn.')
# # returns True
# print(result)

# text = "programming is easy"
# res_1 = text.endswith(('is', 'easy'))  # true
# res_2 = text.endswith(('programming', 'is'))  # false
# print(res_1, res_2)
# str_length = len(text)
# end_with = ('programming', 'is')
# result = text.endswith(end_with, 0, len(text))
# print(result)

# input 39 => 3 + 9 = 12
# type_two_number = input('your number?\n')
# first_digit = type_two_number[0]
# second_digit = type_two_number[1]
# num_1 = int(first_digit)
# num_2 = int(second_digit)
# print(num_1 + num_2)

# PEMDAS
# Parenthese ()
# Exponents **
# Multipication *
# Division /
# Addition +
# Subtraction -
# print(3 * 3 + 3 / 3 - 3)  # 7.0 i want 3.0
# print(3 * (3 + 3) / 3 - 3)

# get the user hight and weight bmi
# height = input('what is your height?\n')
# weight = input('what is your weight?\n')
# bmi = int(weight) / float(height) ** 2
# bmi_int = int(bmi)
# print(bmi_int)
