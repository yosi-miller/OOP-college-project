from collectionmanager import *
from person import *
from data_management import DataManagement


class College:
    def __init__(self, name, db_name):
        self.name = name
        self.studentManger = StudentManager()
        self.setting_data = DataManagement(db_name)

    # def add_student(self, student):
    # self.students.append(student)


mivhar = College("mivhar", "data college")
yosi = Student("yosi", "y@y.com")
axx = Student('asd', 'dc')
mivhar.studentManger.add(yosi)
print(yosi.id)
s = mivhar.studentManger.get_the_name(yosi.id)
print(s)
