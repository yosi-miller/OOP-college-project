from collection_manager import CollectionManager
from student import Student


class StudentsManager(CollectionManager):

    def return_student_by_id(self, student_id):
        """
        this function get student by id
        :param student_id: student_instance.id
        :return:
        """
        for student in self.collection:
            if student.Person_Id == student_id:
                return student.return_student_information()

    def show_all_data(self):
        """
        this function show all students
        :return: all students
        """
        result = []
        for student in self.collection:
            result.append(f"Student name: {student.name}, "
                          f"Student id: {student.Person_Id}, "
                          f"Student email: {student.email}\n")
        return "".join(result) if result else "Don't have a students."

if __name__ == "__main__":
    yosi = Student("yosi", "a@Q")
    a = StudentsManager()
    a.add(yosi)
    print(a.return_student_by_id(yosi.Person_Id))
    print(a.show_all_data())
    aviv = Student("aviv", "b@Q")
    a.add(aviv)
    print(a.show_all_data())
