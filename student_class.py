from person_class import Person

class Student(Person):

    def __init__(self, name, email, instructor):
        Person.__init__(self, name, email)
        # self.__teacher = []
        self.__instructor_name = instructor
        self.__grade_course = {}
        # self.course = [] dont need this variable because we have it in the __teacher class
        # and add __teacher to student so we have to the teacer the course name

    # @property
    # def get_teacher(self):
    #     return self.__teacher

    @property
    def get_instructor_name(self):
        return self.__instructor_name

    def get_student_information(self):
        return f"Student name: {self.get_name}\n"\
               f"Student id: {self.get_Id}\n"\
               f"Student email: {self.get_email}\n"\
               f"Instructor name: {self.__instructor_name}"

    def add_grade_to_student(self, course_instance, grade):
        self.__grade_course[course_instance] = grade

    def show_grade_by_course(self, id_course):
        if id_course in self.__grade_course:
            return f"the grade of the course {id_course} is {self.__grade_course[id_course]}"
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
    print(a.get_student_information)

