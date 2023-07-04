from program_manager import ProgramManager
from courses_manager import CoursesManager
from students_manager import StudentsManager
from teachers_manage import TeachersManager
from programs_manager import ProgramsManagement

class College:

    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.__studentManger = StudentsManager()
        self.__teachersManager = TeachersManager()
        self.__programManager = ProgramManager()
        self.__programsManager = ProgramsManagement()
        self.__coursesManager = CoursesManager()


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
    def programManager(self):
        return self.__programManager

    @property
    def coursesManager(self):
        return self.__coursesManager

    @property
    def programsManager(self):
        return self.__programsManager

    def __str__(self):
        return f"College name: {self.name}, College city: {self.city}"



if __name__ == '__main__':
    pass
    # mivhar = College("mivhar", "tel aviv")
    # yosi = Student("yosi", "d@d.com", "avi")
    # c = Course("math")
    # mivhar.add_student(Student("yosi", "d@d.com", "avi"))


