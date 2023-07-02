from student_class import Student
from teacher_class import Teacher


class Class:

    def __init__(self, teacher_instance, course_instance):
        self.teacher = teacher_instance
        self.__class_course = course_instance
        self.__students = []

    def add_student(self, instance):
        self.__students.append(instance)

    def add_grade_to_student(self, grade, id_student):
        for student in self.__students:
            if student.Id == id_student:
                student.add_grade_to_student(self.__class_course, grade)

    def show_students_class(self, teacher_id):  # כמה תללמידים מלמד
        pass

    def average_tests_all_student(self, course_id):  # ממוצע ציון כיתה פר מקצוע
        pass

    def show_students_grate(self, student_instance):
        """
        this is show grate of the student
        :param student_instance: student instance
        :return: grate of the student
        """
        return student_instance.show_grade_by_course(self.__class_course)

if __name__ == '__main__':
    from course import Course
    from instructor_class import Instructor
    course1 = Course("python")
    instructor = Instructor("avi", "a@a")
    student1 = Student("avi", "a@a", instructor)
    teacher = Teacher("avi", "a@a")
    class1 = Class(instructor, teacher)
    class1.add_student(student1)


