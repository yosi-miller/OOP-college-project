from student_class import Student
class Class:

    def __init__(self, teacher_instance, course_instance):
        self.teacher = teacher_instance
        self.__class_course = course_instance
        self.__students = []

    def add_student(self, instance):
        self.__students.append(instance)

    def add_grade_to_student(self, grade, id_student):
        for student in self.__students:
            if student.get_Id == id_student:
                student.add_grade_to_student(self.__class_course, grade)

    def show_students_class(self, teacher_id):  # כמה תללמידים מלמד
        pass

    def average_tests_all_student(self, course_id):  # ממוצע ציון כיתה פר מקצוע
        pass

    def show_students_grate(self):
        pass
