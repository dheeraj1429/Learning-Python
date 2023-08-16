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

# items = [1,2,3,4]
# print(items[3])

# adding
# new_list = items.append(100)
# new_list = items
# new_list.insert(2, 100)
# print(new_list)
# item_index = items.index(2)
# items.insert(item_index, 2000)
# print(items)
# items.extend([2000])
# print(items)

# removing
# items.pop()
# items.pop(0) # return the removed items
# print(items)
# items.remove(2) # does no return anything
# print(items)
# items.clear() # clear remove all the items from the list.
# print(items) 

# items index     value, start, end
# print(items.index(2, 0, 2))

# to check the element in the list.
# if(2 in items):
#     items.remove(2)
# print(items)

# to check the how many items elements in the list
# print(items.count(2))

# items = ["a", "b", "c", "x", "d", "e", "f"]
# items.sort()
# print(items)
# print(sorted(items))
# print(items)
# items.sort()
# print(items)
# new_items = items[:]
# print(new_items)
# new_items.reverse()
# print(new_items)
# new_list = items[::-1]
# print(new_list)

# items = range(0, 100)
# print(list(items))

# new_sentence = ' '.join(['hi', 'my', 'name', 'is', 'demo'])
# print(new_sentence)

# list unpacking
# a,b,c, *others, d = [1,2,3,4,5,6,7,8]
# print(a)
# print(b)
# print(c)
# print(others)
# print(d)


# Distionary
distionary = {
    "data": [1,2,3,4],
    "a": 10
}


# print(distionary["data"])
# if distionary.get('a'):
#     print(distionary.get('a'))
# if "data" in distionary:
#     print(distionary['data'])
        
# user_2 = dict(name="dheeraj", age=30, email="dheeraj@gmail.com")
# print(user_2)

# print("data" in distionary)

# print('data' in distionary.keys())
# print(10 in distionary.values())

# print(distionary.items())

# distionary.clear()
# print(distionary)

# distionary.pop('a')
# print(distionary)
# distionary.popitem()
# print(distionary)

# distionary.update({'a': 2000})
# print(distionary)
# distionary['a'] = 23000
# print(distionary)

# my_tuple = (1,2,3,4,5)
# print(my_tuple)
# my_tuple[1] = 1
# print(2 in my_tuple)

# my_tuple = {
#     (1,2,3): 'sone new data'
# }
# print(my_tuple[(1,2,3)])

my_tuple = (1,2,3,4,5)
# new_tuple = my_tuple[::2]
# print(new_tuple)
# x = my_tuple[1]
# y = my_tuple[2]
# x,y, *others = my_tuple
# print(x, y, others)
# print(my_tuple.count(2))
# print(my_tuple.index(5))