from person_class import Person


class Teacher(Person):

    def __init__(self, name, email):
        Person.__init__(self, name, email)
        self.profession = []

    def add_profession(self, profession): #הוספת מקצוע
        self.profession.append(profession)

    def remove_profession(self, profession): #הסרת מקצוע
        self.profession.remove(profession)
