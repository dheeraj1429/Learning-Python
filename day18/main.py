# import random
import pandas

# number_list = [1, 2, 3]
# new_list = [n * 2 for n in number_list]
# print(new_list)

# name = 'Dheeraj'
# name_list = [n for n in name]
# print(name_list)

# print([item * 2 for item in range(0, 100)])

# name_list = ["Alex", "John", "Amanda", "Kris"]
# print([letter for letter in name_list if len(letter) < 5])
# print([(letter).upper() for letter in name_list if len(letter) < 5])

# numbers_list = [1, 2, 3, 4, 5, 12]
# print([number**2 for number in numbers_list])
# print([number*number for number in numbers_list])

# data_one = [1, 2, 3, 10, 20]
# data_two = [2, 5, 10, 12]
# set_one = set(data_one)
# set_two = set(data_two)
# common = list(set_one.intersection(set_two))
# print([num for num in data_one if num in data_two])


# name_list = ["Alex", "John", "Amanda", "Kris"]
# students = {student: random.randint(1, 100) for student in name_list}
# print(students)
# passed_students = {key: value for (
#     key, value) in students.items() if value >= 60}
# print(passed_students)

# sentance = 'What is the name of the student'
# new_dict = {letter: len(letter) for letter in sentance.split()}
# print(new_dict)


# weather_c = {
#     "Monday": 12,
#     "Tuesday": 20,
#     'Wednesday': 20,
#     'Thursday': 10,
#     'Friday': 10,
#     'Saturday': 30
# }

# temp_dict = {key: (value * 9/5) + 32 for (key, value) in weather_c.items()}
# print(temp_dict)

# csv_data = pandas.read_csv('./data.csv')
# for (key, value) in csv_data.items():
#     print(value[2])

# for (index, row) in csv_data.iterrows():
#     print(row.code)

# new_dict = {row.letter: row.code for (_, row) in csv_data.iterrows()}
# print(new_dict)
