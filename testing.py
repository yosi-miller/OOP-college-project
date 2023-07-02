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




a = test()
print(a.name)
a.name = "new name"
print(a.name)