class CollectionManager:
    def __init__(self):
        self.collection = []

    def add(self, instance):
        self.collection.append(instance)

    def get(self, id):
        pass

    def remove(self, id):
        pass

    def print_all(self):
        pass


class StudentManager(CollectionManager):
    pass


class TecherManager(CollectionManager):
    pass


class InstrctionManager(CollectionManager):
    pass


class College:
    def __init__(self, name):
        self.name = name
        self.studentManger = StudentManager()

    # def add_student(self, student):
    # self.students.append(student)


class Person:
    id_auto_incremment = 1

    def __init__(self, name, email):
        self.id = Person.id_auto_incremment
        Person.id_auto_incremment += 1
        self.name = name
        self.email = email


class Student(Person):
    pass


class Teacher(Person):
    pass


class Instructor(Person):
    pass


if __name__ == '__main__':
    mivchar = College('michar')

    # yosi = Student('yosi', 'y@yosi.co')
    # yakov = Student('yakov', 'y@yokov.co')

    studentManager = mivchar.studentManger

    studentManager.add_student('yosi', 'y@yosi.co')
    studentManager.add_student('yakov', 'y@yokov.co')
    studentManager.print_all_students()
