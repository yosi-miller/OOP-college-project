from person import Person

class Student(Person):

    def print_student_information(self):
        print(self)

    def __str__(self):
        return f"Teacher name: {self.name},\n" \
               f"Teacher id: {self.Id},\n" \
               f"Teacher email: {self.email}"


if __name__ == '__main__':
    a = Student("avi", "d")
    a.print_student_information()


