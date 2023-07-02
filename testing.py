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




dic = {"a":1, "b": 2, "c": 3}
b = dic.values()
print(sum(b) / len(b))