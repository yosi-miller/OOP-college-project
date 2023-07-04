from person import Person

class Student(Person):

    def return_student_information(self):
        return self

    def __str__(self):
        return f"Teacher name: {self.name},\n" \
               f"Teacher id: {self.Person_Id},\n" \
               f"Teacher email: {self.email}"


if __name__ == '__main__':
    a = Student("avi", "d")
    a.return_student_information()


