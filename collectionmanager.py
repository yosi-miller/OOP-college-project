class CollectionManager:
    def __init__(self):
        self.collection = []

    def add(self, instance):
        self.collection.append(instance)

    def get(self, id):
        for student in self.collection:
            if student.id == id:
                return student.name

    def remove(self, id):
        pass

    def print_all(self):
        pass


class StudentManager(CollectionManager):

    def average_tests(self):
        pass


class TeachersManager(CollectionManager):

    def average_student_tests(self):
        pass



class InstrctionManager(CollectionManager):
    pass
