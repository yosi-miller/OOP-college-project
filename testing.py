# import tkinter as tk
# help(tk)
class test:

    def __init__(self):
        self.__name = "test"
        self.__age = 10

    @property
    def name(self):
        return self.__name
    @property
    def age(self):
        return self.__age

    @name.setter
    def name(self, name):
        self.__name = name

    @age.setter
    def age(self, age):
        self.__age = age

a = test()
print(a.age)
a.age = 20
print(a.age)
