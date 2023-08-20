# loops

# for item in 'some new data':
#     print(item)

# for item in [1,2,3]:
    # print(item)


# for item in (1,2,3,4,5):
#     print(item)
#     # print(item)
#     # print(item)
# print(item) # item == 5

# a = []
# b = [1,2,3]
# c = [1,2,3,4,5]

# for x in b:
#     for y in c:
#         if x == y:
#             a.append(x)

# print(a)

# iterables -> can be a list, tuple, dictionary, set, string.
# iterated items -> one by one check each item in the collection.


# dictionary
# user_info = {
#     "name": "dheeraj",
#     "age": 23,
#     "place": "new delhi"
# }

# for item in user_info:
#     print(user_info[item])
    
# for x in user_info.items():
#     print(f"{x[0]}: {x[1]}")

# for x in user_info.items():
#     key,value = x
#     print(f'{key}:{value}')

# for key, value in user_info.items():
#     print(f'{key}:{value}')

# counter
# my_list = [1,2,3,4,5,6,7,8,9,10,11,12]
# sum = 0
# for item in my_list:
#     sum += item
# print(f'sum: {sum}')

# for _ in range(0, 10):
#     print(f'some outout count')


# for i,char in enumerate('this is some new string'):
#     print(i, char)
    
# for char in 'this is some new string':
#     print(char)


# while loop
# count = 0
# while count < 20:
#     print(count)
#     count +=1
#     break
# else:
#     print('loop is over')

# my_list = [1,2,3]
# for item in my_list:
#     print(item)
    
# i = 0
# while i < len(my_list):
#     print(my_list[i])
#     i += 1


# while True:
#     response = input('What do you want to do ?\n')
    
#     if(response == 'bye'):
#         break

# my_list = [1,2,3]
# for item in my_list:
#     # print(item)
#     pass

# i = 0
# while i < len(my_list):
#     print(my_list[i])
#     i += 1

# Picture = [
#     [0,1,1,0,1,1,0],
#     [1,1,1,1,1,1,1],
#     [1,1,1,1,1,1,1],
#     [0,1,1,1,1,1,0],
#     [0,0,1,1,1,0,0],
#     [0,0,0,1,0,0,0]
# ]

# for image in Picture:
#     for pixel in image:
#         if pixel == 1:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print('')

# some_list = ['a', 'b', 'c', 'd', 'e', 'f', 'a', 'c']
# duplicates = []

# for item in some_list:
#     itemCount = some_list.count(item)
#     if itemCount > 1:
#         is_exists = item in duplicates
#         if not is_exists:
#             duplicates.append(item)

# print(duplicates)


# functions
# def -> defiend

# def some_function():
#     print('some data we want to print')
    
# # some_function()
# some_function = 19
# print(some_function)

# parameters
# def some_funciton(user_name):
#     print(f'hello {user_name}')

# # arguments
# some_funciton('dheeraj')

# def logger_function(name, log):
#     print(f'your name is {name} and the log is {log}') 


# positional arguments
# logger_function('dheeraj', 'some data we want to print')
# logger_function('some data we want to print', 'dheeraj')

# keyword arguments
# logger_function(log='some data we want to print',name='dheeraj')

# return
# def sum_function(num_one, num_two):
#     return num_one + num_two

# print(sum_function(10, 20))

# function inside another function
# def sum(num_one, num_two):
#     def another_function(num_one, num_two):
#         return num_one + num_two
#     return another_function(num_one, num_two)

# print(sum(10, 10))


# Docstrings

# def one():
#     '''
#     info: this function is returning the number of elements of the array.
#     '''
#     return []
