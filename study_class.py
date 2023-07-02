from student import Student
from teacher import Teacher

class StudyClass:

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
        all_students = []
        for i, student in enumerate(self.__students):
            all_students.append(student.name)
            if i != len(self.__students) - 1:  # Check if it's not the last student
                all_students.append("\n")
        return "".join(all_students)

    def average_test_students(self):
        """
        this is average test of all students in the class
        :return: average test of all students in the class
        """
        return sum(self.__grade_course_students.values()) / len(self.__grade_course_students)

    def class_information(self):
        return self

    def __str__(self):
        return f"In this class learn: {self.course_name}, "\
               f"Teacher name: {self.teacher.name}, "\
               f"Amount students: {len(self.__students)}"


if __name__ == '__main__':
    student1 = Student("avi", "a@a")
    student2 = Student("yosi", "a@a")
    teacher = Teacher("avi", "a@a")
    class1 = StudyClass(teacher,"english")
    class1.add_student(student1)
    class1.add_student(student2)
    class1.add_grade_to_student(100, student1.Id)
    class1.add_grade_to_student(90, student2.Id)
    print(class1.show_students_class())
    print(class1.average_test_students())
    print(class1.class_information())




