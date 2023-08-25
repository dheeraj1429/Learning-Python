# def multiply_2(li):
#     new_list = []
#     for item in li:
#         new_list.append(item*2)
#     return new_list


# print(multiply_2([1, 2, 3]))

# map, filter, zip, and reduce
# def action(item):
#     return item * 2


# print(list(map(action, [1, 2, 3])))

# def check_odd(item):
#     return item % 2 == 0


# print(list(filter(check_odd, [1, 2, 3])))

# zip
# print(list(zip([1, 2, 3], [4, 5, 6], [10, 11, 12])))

# reduce
# from functools import reduce


# def accumulator(acc, item):
#     return acc + item


# print(reduce(accumulator, [1, 2, 3], 0))

# def accumulator(li):
#     sum = 0
#     for item in li:
#         sum += item
#     return sum


# print(accumulator([1, 2, 3]))

# labda function

# print(list(map(lambda item: item * 2, [1, 2, 3])))

# my_list = [1, 2, 3]
# print(list(map(lambda item: item * 2, my_list)))

# a = [(1, 2), (2, 4), (10, -1), (9, 1)]
# a.sort(key=lambda item: item[1])
# print(a)

# List comprehension
# my_list = [item for item in 'hello']
# for char in 'hello':
#     my_list.append(char)
# print(my_list)
# print(list(num for num in range(0, 10)))
# print(list(num ** 2 for num in range(0, 10)))
# print(list(num**2 for num in range(0, 10) if num % 2 == 0))

# set comprehension
# print(set(item for item in 'hello'))
# print(set(num for num in range(0, 10)))
# print(set(num**2 for num in range(0, 10)))
# print(set(num**2 for num in range(0, 10) if num % 2 == 0))

# dictionary comprehension
# dict = {key: value}
# simple_dictionary = {"a": 1, "b": 2}
# print({key: value**2 for key, value in simple_dictionary.items()})
# print({key: value**2 for key, value in simple_dictionary.items() if value % 2 == 0})
# print({num: num*2 for num in [1, 2, 3]})

# some_list = [item for item in 'hellowerrandlhe']
# duplicates = list(set(item for item in some_list if some_list.count(item) > 1))
# print(duplicates)
