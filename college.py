from classes_manager import ClassesManager
from student import Student
from students_manager import StudentsManager
from teachers_manage import TeachersManager

class College:

    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.__studentManger = StudentsManager()
        self.__teachersManager = TeachersManager()
        self.__classesManager = ClassesManager()


    @property
    def college_city(self):
        return self.city

    @property
    def college_name(self):
        return self.name

    @college_city.setter
    def college_city(self, new_city):
        self.city = new_city

    @college_name.setter
    def college_name(self, new_name):
        self.name = new_name

    @property
    def studentManger(self):
        return self.__studentManger

    @property
    def teachersManager(self):
        return self.__teachersManager

    @property
    def classesManager(self):
        return self.__classesManager

    def __str__(self):
        return f"College name: {self.name}, College city: {self.city}"



if __name__ == '__main__':
    mivhar = College("mivhar", "tel aviv")
    yosi = Student("yosi", "d@d.com", "avi")
    c = Course("math")
    mivhar.add_student(Student("yosi", "d@d.com", "avi"))


