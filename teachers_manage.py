from collection_manager import CollectionManager
from teacher import Teacher

class TeachersManager(CollectionManager):

    def return_teacher_by_id(self, teacher_id):
        """
        get teacher by id
        :param teacher_id: instance_teacher.id
        :return: information about teacher
        """
        for teacher in self.collection:
            if teacher.Person_Id == teacher_id:
                return teacher.return_teacher_information()

    def show_all_data(self):
        """
        this function return all information about teachers
        :return: list of all teachers
        """
        data = []
        for TEACHER in self.collection:
            data.append(f"name: {TEACHER.name}, id: {TEACHER.Person_Id}, email: {TEACHER.email}\n")
        return "".join(data)


if __name__ == '__main__':
    me = TeachersManager()
    teacher = Teacher("moshe", "m@m.com")
    teacher1 = Teacher("david", "a@a.com")
    me.add(teacher)
    me.add(teacher1)
    # a = me.get_courses_for_teacher(teacher.get_Id)
    # print(me.return_teacher_by_id(teacher.Person_Id))
    print(me.show_all_data())