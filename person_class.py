class Person:
    id_auto_incremment = 1

    def __init__(self, name, email):
        self.__id = Person.id_auto_incremment
        Person.id_auto_incremment += 1
        self.__name = name
        self.__email = email

    @property
    def get_Id(self):
        return self.__id

    @property
    def get_name(self):
        return self.__name

    @property
    def get_email(self):
        return self.__email
