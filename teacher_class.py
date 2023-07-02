from person_class import Person

class Teacher(Person):

    def __init__(self, name, email, course_instance):
        Person.__init__(self, name, email)
        self.__course = course_instance

    @property
    def get_course(self):
        return self.__course

    @property
    def get_information_teacher(self):
        return f"Teacher name: {self.get_name},\n" \
               f"Teacher id: {self.get_Id},\n" \
               f"Teacher email: {self.get_email},\n" \
               f"Teacher course: {self.get_course.get_name}"



if __name__ == '__main__':
    from course import Course
    course = Course("python")
    teacher = Teacher("avi", "a@a", course)
    print(teacher.get_information_teacher)
