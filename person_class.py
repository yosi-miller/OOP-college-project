class Person:
    id_auto_incremment = 1

    def __init__(self, name, email):
        self.__id = Person.id_auto_incremment
        self.__name = name
        self.__email = email
        Person.id_auto_incremment += 1

    @property
    def Id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email
