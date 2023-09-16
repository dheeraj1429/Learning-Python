# import pandas

# # with open("data.txt", mode='r') as data_file:
# #     content = data_file.read()
# #     new_content = content.replace('some', "dome")
# #     print(new_content)

# # # create a file automatic for you if file is not exists,
# # with open("data.txt", mode='w') as file:
# #     file.write("some content we want to add on this file.")

# # with open("data.txt", mode='a') as file:
# #     file.write("\nsome content we want to append on this file.")

# # file = open("data.txt", mode='r')
# # print(file.readline())

# # txt = '   some    '
# # print(txt.strip())

# # with open("data.txt", mode='r') as file:
# #     new_content = file.readlines()
# #     print(new_content)

# # import csv

# # with open("./p.csv") as file:
# #     data = csv.reader(file)
# #     for row in data:
# #         print(row)

# import pandas

# csv_data = pandas.read_csv('./p.csv')
# # print(csv_data['X'])
# # print(csv_data)
# # print(type(csv_data))
# # print(type(csv_data['X']))
# # dict_data = csv_data.to_dict()
# # print(dict_data)

# # list_data = csv_data['X'].to_list()
# # print(list_data)
# print(csv_data[csv_data['day'] == 'monday'])
# print(csv_data[csv_data["age"] == csv_data["age"].max()])

# data = pandas.read_csv("./task.csv")
# print(data.head(33))
# print(data.tail(10))
# day_column = data[data['age'] >= 20]
# print(day_column.day[1])

# data_dict = {
#     "student": ["Any", "Jammes", "Anna"],
#     "score": [20, 30, 10]
# }

# dict_data_frame = pandas.DataFrame(data_dict)
# print(dict_data_frame)


# data_dict = {
#     "name": ["Dheeraj"],
#     "age": [21],
#     "place": ["New delhi"]
# }

# dict_data_frame = pandas.DataFrame(data_dict)
# dict_data_frame.to_csv('new.csv')


# ---------

# data = pandas.read_csv(
#     './2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# primary_cl = data["Primary Fur Color"]

# gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

# dict_data_frame = {
#     "Fur color": ['Gray', "Red", "Black"],
#     "length": [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
# }

# data_frame = pandas.DataFrame(dict_data_frame)
# data_frame.to_csv('squirrel_data.csv')
