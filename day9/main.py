# def hello():
#     print('hello')


# greet = hello
# del hello
# print(greet())

# higher order function HOC
# def greet(fn, *args):
#     fn(*args)


# def printFn(*args):
#     print(*args)


# greet(printFn, [1, 2, 3])

# Decorator


# def my_decorator(func):
#     def wrap_func():
#         print('*******')
#         func()
#         print('*******')
#     return wrap_func


# @my_decorator
# def hello():
#     print('hello')


# hello()

# my_decorator(hello)()

# def my_decorator(func):
#     def wrap_func(*args, **kwargs):
#         func(*args, **kwargs)
#     return wrap_func


# @my_decorator
# def hello(value):
#     print(value)


# hello('hi')
from time import time


# def performance(func):
#     def wrapped_func(*args, **kwargs):
#         t1 = time()
#         func(*args, **kwargs)
#         t2 = time()
#         print(f' took {t2 - t1} seconds')
#     return wrapped_func


# @performance
# def long_time():
#     for item in range(100000):
#         item*5


# long_time()
