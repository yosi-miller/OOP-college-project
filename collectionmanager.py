class CollectionManager:
    def __init__(self):
        self.collection = []

    def add(self, instance):
        self.collection.append(instance)

    def get_the_name(self, id):
        for student in self.collection:
            if student.id == id:
                return student.name


    def remove(self, id):
        pass

    def print_all_students(self):
        pass


class StudentManager(CollectionManager):
    def average_tests_all_student(self, profession): #ממוצע ציון כיתת פר מקצוע
        pass

    def average_tests_student(self, id, profession):
        pass

    def get_the_amount_of_student(self):
        pass


class TeachersManager(CollectionManager):

    def get_the_amount_of_student(self): #כמה תללמידים מלמד
        pass

    def get_the_student_names(self): #שמות התלמידים של המדריך
        pass

    def get_the_profession(self, id): # איזה מקצועות יש למורה (על ידי זיהוי id)
        pass


class InstrctionManager(CollectionManager):

    def get_the_amount_of_student(self): #כמה תללמידים מדריך
        pass

    def get_the_student_names(self): #שמות התלמידים של המדריך
        pass