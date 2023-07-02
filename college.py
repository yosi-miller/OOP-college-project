from course import Course
from student import Student
from students_manager import StudentsManager
from teachers_manage import TeachersManager


class College:

    def __init__(self, name, city):
        self.name = name
        self.__studentManger = StudentsManager()#private
        self.__teachersManager = TeachersManager()
        self.city = city

    @property
    def get_data_college(self):
        return f"College name: {self.name}, College city: {self.city}"

    @property
    def college_city(self):
        return self.city

    def add_student(self, student):
        self.__studentManger.add(student)



mivhar = College("mivhar", "tel aviv")
yosi = Student("yosi", "d@d.com", "avi")
c = Course("math")
mivhar.add_student(Student("yosi", "d@d.com", "avi"))


