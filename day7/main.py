# oop
# class Person:  # Class
#     pass


# # Instanciate new Person class which is return new Person object.
# newPerson = Person()
# print(type(Person))
# print(type(newPerson))

# class Person:
#     def __init__(self, name):
#         self.name = name

#     def run(self):
#         print(self.name)


# newPerson = Person('Dheeraj')
# print(newPerson.run())


# class ListItem:
#     members = True  # Class object attributes
#     _even_numbers = []

#     def __init__(self, list_item):
#         self.list_item = list_item  # attributes
#         self._even_numbers = self._even_numbers
#         self.temp = list_item[0]

#     def highest_even(self):
#         for element in self.list_item:
#             if element % 2 == 0:
#                 self._even_numbers.append(element)

#         for item in self._even_numbers:
#             if self.temp < item:
#                 self.temp = item
#         return self.temp

#     @classmethod
#     def List_even_numbers(self):
#         return self._even_numbers

#     @classmethod
#     def add_number(cls, num_1, num_2):
#         return num_1 + num_2

#     @staticmethod
#     def inc_number(num_1, num_2):
#         return num_1 + num_2


# list_item = [10, 20, 30, 10, 14, 200, 100, 20]
# new_list = ListItem(list_item)
# print(new_list.highest_even())
# print(new_list.List_even_numbers())
# print(new_list.add_number(10, 20))
# print(ListItem.add_number(10, 20))
# print(ListItem.inc_number(29, 29))

# some_dict = {"name": "dheeraj", "age": 21}
# print(some_dict['name'])
# print(some_dict.name)

# print(new_list.highest_even())
# new_list._even_numbers = 'some new data'
# print(new_list._even_numbers)


# class Person():
#     def __init__(self, name):
#         self.name = name

#     def logger(self):
#         print('log Person')

#     def print_name(self):
#         print('name: %s' % self.name)

# class Teacher(Person):
#     def __init__(self, task, name):
#         # Person.__init__(self, name)
#         super().__init__(name)
#         self.task = task

#     def task(self):
#         print('log Teacher')


# class Student(Teacher):
#     def error(self):
#         print('print some error message')


# student_1 = Student()
# print(student_1.logger())
# print(student_1.task())
# print(isinstance(student_1, Student))

# teacher_one = Teacher('new class join', 'Dheeraj')
# print(teacher_one.print_name())

# interspection

# MRO -> Method Resolution Order
# class A:
#     num = 10


# class B(A):
#     num = 20


# class C:
#     def log(self):
#         print('some data')


# class D(C, B):
#     num = 50


# e = D()
# print(e.num)
