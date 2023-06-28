class Person:
    id_auto_incremment = 1

    def __init__(self, name, email):
        self.id = Person.id_auto_incremment
        Person.id_auto_incremment += 1
        self.name = name
        self.email = email



