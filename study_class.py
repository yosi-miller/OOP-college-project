from student import Student
from teacher import Teacher
from course import Course

class StudyClass:
    __Class_Id = 100

    def __init__(self, teacher_instance, course_instance):
        self.__teacher = teacher_instance
        self.__course = course_instance
        self.__id = StudyClass.__Class_Id
        self.__students = []
        self.__grade_course_students = {}
        StudyClass.__Class_Id += 100

    @property
    def course(self):
        return self.__course

    @property
    def students(self):
        return self.__students

    @property
    def students_grade(self):
        return self.__grade_course_students

    @property
    def Class_Id(self):
        return self.__id

    @property
    def class_teacher(self):
        return self.__teacher

    @class_teacher.setter
    def class_teacher(self, new_name):
        self.__teacher = new_name

    def remove_student(self):
        pass

    def change_grade(self):
        pass

    def add_student(self, instance):
        self.__students.append(instance)

    def add_grade_to_student(self, grade, id_student):
        self.__grade_course_students[id_student] = grade

    def show_all_students_class(self):
        """
        show all students in the class
        :return: all students in the class
        """
        num = 1
        all_students = [f"{self.course.name} Course:\n"]
        for i, student in enumerate(self.__students):
            all_students.append(f"{num}: {student.name}")
            num += 1
            if i != len(self.__students) - 1:  # Check if it's not the last student
                all_students.append("\n")
        return "".join(all_students) if len(all_students) > 1 else "Don't have a "

    def average_test_students(self):
        """
        this is average test of all students in the class
        :return: average test of all students in the class
        """
        return sum(self.__grade_course_students.values()) / len(self.__grade_course_students)

    def class_information(self):
        return self

    def __str__(self):
        return f"In this class learn: {self.course.name}, "\
               f"Teacher name: {self.class_teacher.name}, "\
               f"Amount students: {len(self.__students)}"


if __name__ == '__main__':
    student1 = Student("avi", "a@a")
    student2 = Student("yosi", "a@a")
    teacher = Teacher("avi", "a@a")
    class1 = StudyClass(teacher,"english")
    class1.add_student(student1)
    class1.add_student(student2)
    class1.add_grade_to_student(100, student1.Person_Id)
    class1.add_grade_to_student(90, student2.Person_Id)
    print(class1.show_all_students_class())
    # print(class1.average_test_students())
    # print(class1.class_information())




