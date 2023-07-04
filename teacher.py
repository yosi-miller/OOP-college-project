from person import Person

class Teacher(Person):

    def return_teacher_information(self):
        return self

    def __str__(self):
        return f"Teacher name: {self.name},\n" \
               f"Teacher id: {self.Person_Id},\n" \
               f"Teacher email: {self.email}"


if __name__ == '__main__':
    teacher = Teacher("avi", "a@a")
    teacher.return_teacher_information()
