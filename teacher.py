from person import Person

class Teacher(Person):

    def __init__(self, name, email):
        Person.__init__(self, name, email)

    def print_teacher_information(self):
        print(self)

    def __str__(self):
        return f"Teacher name: {self.name},\n" \
               f"Teacher id: {self.Id},\n" \
               f"Teacher email: {self.email}"


if __name__ == '__main__':
    teacher = Teacher("avi", "a@a")
    teacher.print_teacher_information()
