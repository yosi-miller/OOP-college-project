from person_class import Person
from course import Course

class Student(Person):

    def __init__(self, name, email, instructor):
        Person.__init__(self, name, email)
        self.__instructor_name = instructor
        self.__grade_course = {}
        # self.course = [] dont need this variable because we have it in the __teacher class
        # and add __teacher to student so we have to the teacher the course name
        # self.__teacher = []

    # @property
    # def get_teacher(self):
    #     return self.__teacher

    @property
    def instructor_name(self):
        """
        get the name of the instructor
        :return: instructor name
        """
        return self.__instructor_name

    def show_student_information(self):
        return f"Student name: {self.name}\n"\
               f"Student id: {self.Id}\n"\
               f"Student email: {self.email}\n"\
               f"Instructor name: {self.__instructor_name}"

    def add_grade_to_student(self, course_instance, grade):
        self.__grade_course[course_instance] = grade

    def show_grade_by_course(self, inctance_course):
        if inctance_course in self.__grade_course:
            return f"the grade of the course {inctance_course.name} is {self.__grade_course[inctance_course]}"
        return "Don't have a grads to the student"

    @property
    def all_grades(self):
        results = []
        if len(self.__grade_course) > 1:
            for key, value in self.__grade_course.items():
                results.append(f"the grade of the course {key} is {value}\n")
            return results
        return "Don't have a grads to the student"

    # def add_teacher(self, teacher):
    #     """
    #     add instance of __teacher to student
    #     :param teacher: instance of __teacher
    #     :return: none
    #     """
    #     self.__teacher.append(teacher)


if __name__ == '__main__':
    a = Student("avi", "d", "avi")
    a.add_grade_to_student("math", 100)
    a.add_grade_to_student("english", 90)
    print(a.show_student_information)

