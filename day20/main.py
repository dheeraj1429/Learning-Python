# Errors handling

# try:
#     with open("data.txt", 'r') as file:
#         print(file)
# except:
#     print("Error reading data file")
# else:
#     print("Success")
# finally:
#     print("this run always succeeds")

# if we want to create a file without getting the errors
# try:
#     with open("./data.txt", 'r') as file:
#         print(file, 'file found inside the try statement')
# except:
#     with open("./data.txt", 'w') as file:
#         print(file, 'file is created inside the except statement')


# with open("data.txt", 'w') as file:
#     file.write("some data we want to add to the file....")


# # if we are using the try and except statement like this the excpet block will ignore all the errors.
# try:
#     with open("./data.txt", 'r') as file:
#         print(file, 'file found inside the try statement')
    
#     #  throw the exception but ignore by the except statement.
#     user_info_dict = {"name": "demo", "email": "demo@email.com"}
#     print(user_info_dict["color"])
    
# except:
    
#     # we have to create a file if the file is not exitst. right ? but we are not caching any errors.
#     with open("./data.txt", 'w') as file:
#         print(file, 'file is created inside the except statement')

# first time we don't get the error message,
# try:
#     with open("./data.txt", 'r') as file:
#         print(file, 'file found inside the try statement')
#     user_info_dict = {"name": "demo", "email": "demo@email.com"}
#     print(user_info_dict["color"])
# except FileNotFoundError:
#     file = open("./data.txt", 'w')
#     print(file, 'file is created inside the except statement')
# except KeyError:
#     print("Error key not found")

# try:
#     file = open('./data.txt', 'r')
#     print(file)
# except:
#      file = open('./data.txt', 'w')
#      file.write('some data added to the file...')
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print('this will run allways')

# how to create our own exception
# height = float(input('Height: '))
# weight  = float(input('Weight: '))

# if height >= 30:
#     raise ValueError("Height must be between 30")
# else:
#     bmi = weight / (height ** 2)
#     print(bmi)

# some error
# user_data = [
#     {"likes": 20, "name": "karan"},
#     {"likes": 20, "name": "Rohan"},
#     {"likes": 20, "name": "Sma"},
#     {"name": "Uama"},
#     {"likes": 20, "name": "OR"},
# ]

# total_likes = 0

# for item in user_data:
#     try:
#         total_likes += item['likes']
#     except:
#         pass
    
# print(total_likes)

# import pandas

# data = pandas.read_csv('./data.csv')
# some_dict = {row['letter']:row['code'] for (row_index, row) in data.iterrows()}
# for (row_index, row) in data.iterrows():
#     print(row['letter'])
#     print(row['code'])

# while True:
#     try:
#         word = input("Please enter your word ").upper()
#         output_list = [some_dict[letter] for letter in word]
#     except KeyError:
#         print("Sorry, Please enter only letters")
#     else:
#         print(output_list)
#         break

# import json

# user_data = [
#     {"likes": 20, "name": "karan"},
#     {"likes": 20, "name": "Rohan"},
#     {"likes": 20, "name": "Sma"},
#     {"name": "Uama"},
#     {"likes": 20, "name": "OR"},
# ]

# json_data = json.dumps(user_data)

# add data in json format
# with open('data.json', 'w') as file:
#     file.write(json_data)

# read the json data
# with open('data.json', 'r') as file:
#     print(json.load(file))

# update the json data
# with open('data.json', 'r') as file:
#     user_data_json = json.load(file)

# user_list = list(user_data_json)
# user_list.append({"likes": 10, "name": "some new name"})
# json_dm = json.dumps(user_list)

# with open("data.json", 'w') as js:
#     js.write(json_dm)


