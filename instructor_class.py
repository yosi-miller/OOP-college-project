from person_class import Person


class Instructor(Person):

    def __init__(self, name, email):
        Person.__init__(self, name, email)