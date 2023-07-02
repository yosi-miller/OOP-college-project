from person import Person

class Student(Person):

    def __init__(self, name, email):
        Person.__init__(self, name, email)


    def show_student_information(self):
        return f"Student name: {self.name}\n"\
               f"Student id: {self.Id}\n"\
               f"Student email: {self.email}"

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


if __name__ == '__main__':
    a = Student("avi", "d")
    a.add_grade_to_student("math", 100)
    a.add_grade_to_student("english", 90)
    # print(a.show_student_information)
    print(__name__)

