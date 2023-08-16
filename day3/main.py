import datetime

# print("Learing control Flow and Logical Operators")
# height = int(input('what is your height Cm? \n'))

# if (height >= 90):
#     print('you can right in rolercoster')
# else:
#     print('your have not access to ride. Sorry!')

# num = int(input('Please pic one of the number\n'))

# if (num % 2 == 0):
#     print('number is even')
# else:
#     print('numder is odd')

# height = int(input("what is your height Cm? \n"))

# if height >= 150:
#     age = int(input("What is your age? \n"))
#     if age < 12:
#         print("you have to pay only $5 extra to ride")
#     elif age <= 12 & age >= 18:
#         print("you have to pay only $7 extra to ride")
#     else:
#         print("you have to pay $12 extra to ride")
# else:
#     print("your have not access to ride. Sorry!")

# year = int(input("Which year you want to check\n"))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leep year")
#     else:
#         print("Leep year")
# else:
#     print("leep year")


# height = int(20)

# if height >= 20:
#     print('height is greater then or equl to 20')
# elif height >= 20 and height <= 25:
#     print('height is greater 20 and less then 25')
# elif height < 20:
#     print('height is less then 20')

# my_name = "Dheeraj"
# lower_case_name = my_name.lower()

# fundamentally data types.
# data types 
int # represents all the number
float # represents the number of decimal
str # represents the string
bool # represents the boolean
list # represents the list
tuple # represents the tuple
set # represents the set 
dict # represents the dictionary

# classes -> custom type

# Specilized Data types.

None # repersents the absence of the value.

# print(type(2 + 2))
# print(type(2 / 2))

# print(3 // 2)
# print(10 % 3)

# math functions
# round_number = round(20.6)
# print(round_number)
# print(abs(-20.7))

# num = 2
# num_bin= bin(num)
# print(num_bin)
# int_number = int(num_bin, 2)
# print(int_number)

# constants
# PI = 20
# print(PI)

# a,b,c = 1,2,3
# print(a,b,c)

# augmented assgnments operators
# some_value = 2
# some_value += 2
# print(some_value)

# Escape Sequence
# test = 'this\' "is new" test'
# print(test)

# formate string
# name = 'Dheeraj'
# print(f'hello my name is {name}')

# indexing with strings
# my_name = 'Dheeraj'
# print(my_name[1])

# str_num = '123456'
# [start:end:stepover]
# print(str_num[0:3:2])
# print(str_num[1:])
# print(str_num[:2])
# print(str_num[::2])
# print(str_num[-2])
# print(str_num[::-1])
# print(str_num[::-2])
# for x in str_num:
    # print(x)
    
# print(len(str_num))

# year = datetime.date.today().year
# birthday_year =  input('What is your birth data year?\n')
# current_year = year - int(birthday_year)
# print(f'hww you are {current_year} years old')

items = [1,2,'some other data', 'new item']
print(items[3])