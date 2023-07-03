# import tkinter as tk
# help(tk)

class test:

    def __init__(self):
        self.__id = 1
        self.__name = "name"
        self.__email = "email"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name




a = {}
# while True:
#     key = input("enter name: ")
#     value = input("enter email: ")
#     if key not in a:
#         a[key] = [value]
#     else:
#         a[key].append(value)
#     print(a)
#     if input("enter q to quit: ") == "q":
#         break
c = {"a":[1,2,3,4,5,6,7,8,9,10], "b":[1,2,3,4,5,6,7,8,9,10]}
for k, v in c.items():
    print(k, ", ".join([str(i) for i in v]), sep=": ")

a = [1,2,3,4,5,6,7,8,9,10]
# print(", ".join([str(i) for i in a]))