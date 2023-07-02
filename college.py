from course import Course
from instrction_manager import InstrctionManager
from data_management import DataManagement
from student_class import Student
from students_manager import StudentsManager
from teachers_manage import TeachersManager


class College:
    colleges = []
    id_collage = 1

    def __init__(self, name, city, db_name="college.db"):
        self.name = name
        self.id = College.id_collage
        self.__studentManger = StudentsManager()#private
        self.__teachersManager = TeachersManager()
        self.__instrctionManager = InstrctionManager()
        self.city = city
        # self.setting_data = DataManagement(db_name)
        College.id_collage += 1

    def add_college(college_name):
        College.colleges.append(college_name)

    def remove_college(self, college):
        self.colleges.remove(college)

    @property
    def amount_college(self):
        return len(College.colleges)

    @property
    def get_data_college(self):
        return f"College name: {self.name} , College id: {self.id} , College city: {self.city}"

    @property
    def college_city(self):
        return self.city

    def amount_college_city(city_name):
        amount = 0
        for college in College.colleges:
            if college.city == city_name:
                amount += 1
        return amount

    def add_student(self, student):
        self.__studentManger.add(student)



mivhar = College("mivhar", "tel aviv")
yosi = Student("yosi", "d@d.com", "avi")
c = Course("math")
mivhar.add_student(Student("yosi", "d@d.com", "avi"))


