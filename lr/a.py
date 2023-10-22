# a = 10


# def some_func():
# a = 20
# print(a)
# pass


# some_func()

# print([num for num in range(0, 10)])
# print([num for num in range(0, 100) if num > 10])
# print([num for num in range(0, 100) if num % 2 == 0])
# print([num if num > 10 else 0 for num in range(0, 100)])
# inventory_names = ['Screw', 'Wheel', 'Metal', 'Wood']
# inventory_numbers = [20, 24, 25, 27]
# print([(name, number) for (name, number) in zip(
#     inventory_names, inventory_numbers) if number > 20])
# print([[x for x in range(5)] for y in range(5)])
# combine_list = [[(x, y) for x in range(5)] for y in range(5)]
# for row in combine_list:
#     print(row)

# chess_board = [[f'{letter}{x}' for x in range(
#     1, 9)] for letter in 'ABCDEFGH'[::-1]]
# for row in chess_board:
#     print(row)
# my_dict = {num: num * 2 for num in range(100)}
# print(my_dict)

# sorted
# my_list = [123, 12412, 23, 44, 12, 11, 3, 21201, 122]
# my_list.sort()
# print(my_list)
# print(sorted(my_list, reverse=True))
# print(my_list)

# list2 = [("a", 3), ('b', 3), ('c', 4), ('d', 6), ('e', 10)]
# def sort_function(item):
#     return item[1]
# sort_list = sorted(list2, key=sort_function)
# sort_list = sorted(list2, key=lambda item: item[1])
# print(sort_list)

# my_list = [123, 12412, 23, 44, 12, 11, 3, 21201, 122]
# new_list = list(map(lambda item: item**2, my_list))
# filter_list = list(filter(lambda item: item < 15129, new_list))
# print(filter_list)

# some_data = [{'name': "karan"}, {'name': "dheeraj"}]
# find_doc = list(filter(lambda item: item['name'] == 'karan', some_data))
# print(find_doc[0])

# a = [1, 2, 3]
# print(a[1])
# del a[1]
# print(a[1])
# print(a)
