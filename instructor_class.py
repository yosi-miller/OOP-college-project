from person_class import Person

class Instructor(Person):

    def __init__(self, name, email):
        Person.__init__(self, name, email)
        self.__student = []

    def add_student(self, student):
        """
        add student to instructor
        :param student: instance of student
        :return: none
        """
        self.__student.append(student)

    @property
    def show_students(self):
        """
        show all student for instructor
        :return: none
        """
        student_num = 1
        students = [f"You have{len(self.__student)} students, they are:\n"]
        for student in self.__student:
            students.append(f"{student_num:}{student.name}\n")
            student_num += 1
        return students
