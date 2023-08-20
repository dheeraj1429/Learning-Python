# clean code
# def is_even(num):
#     return num % 2 == 0

# print(is_even(20))

# *args **kwargs

# def super_function(*args):
#     print(*args)

# super_function(1,2,3,4,4,5)

# def super_function(**kwargs):
#     print(kwargs)

# super_function(num=1, num_2=2)

# def highest_even(li):
#     even_numbers =[]
#     temp = li[0]

#     for element in li:
#         if element % 2 == 0:
#             even_numbers.append(element)

#     for item in even_numbers:
#         if temp < item:
#             temp = item
#     return temp

# print(highest_even([10,20,30,10,14,200,100,20]))


# Walrus Oprator
# :=

# a = 'helloooooooo'
# if (string_length := len(a)) > 10:
#     print(f'too long string with {string_length} characters')

# while (n := len(a)) > 1:
#     print(n)
#     a = a[:-1]

# print('done')


# Scope - What variables do i have access to?
# global scope
# function scope

# a = 10
# def some_fun():
#     a = 20
#     return a

# print(a)
# print(some_fun())
# print(a)\

# a = 10
# def some_fun():
#     global a
#     a = 20
#     return a

# print(some_fun())
# print(a)

# a = 10
# def some_fun(a):
#     a += 20
#     return a

# print(some_fun(some_fun(a)))


# nonlocal variables
# def outer():
#     x = 'outer'

#     def inner():
#         nonlocal x
#         x = 'nonlocal'
#         print('inner', x)

#     inner()
#     print('outer', x)


# outer()
