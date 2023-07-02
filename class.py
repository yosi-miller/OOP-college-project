from student import Student
from teacher import Teacher

class Class:

    def __init__(self, teacher_instance, course_name):
        self.teacher = teacher_instance
        self.__course_name = course_name
        self.__students = []
        self.__grade_course_students = {}

    @property
    def course_name(self):
        return self.__course_name

    def add_student(self, instance):
        self.__students.append(instance)

    def add_grade_to_student(self, grade, id_student):
        self.__grade_course_students[id_student] = grade

    def show_students_class(self):
        """
        show all students in the class
        :return:
        """
        pass

    def average_test_students(self):
        """
        this is average test of all students in the class
        :return:
        """
        pass

    def print_class_information(self):
        pass

    def __str__(self):
        return f"Class name: {self.__course_name}\n" \
                  f"Class teacher: {self.teacher.name}\n" \

if __name__ == '__main__':
    student1 = Student("avi", "a@a",)
    teacher = Teacher("avi", "a@a")
    class1 = Class(teacher)
    class1.add_student(student1)


