from collection_manager import CollectionManager
from teacher import Teacher

class TeachersManager(CollectionManager):

    def return_name_teacher_by_id(self, teacher_id):
        """
        return name teacher by id
        :param teacher_id:
        :return:
        """
        for teacher in self.__collection:
            if teacher.Id == teacher_id:
                return teacher.name

    def get_course_for_teacher(self, teacher_id):
        """
        get all courses for teacher
        :return: list of all courses
        """
        for teacher in self.collection:
            if teacher.Id == teacher_id:
                return teacher.get_course.name

    @property
    def teachers(self):
        """
        this function return all information about teachers
        :return: list of all teachers
        """
        data = []
        for TEACHER in self.collection:
            data.append(f"name: {TEACHER.name}, id: {TEACHER.Id}, email: {TEACHER.email}, course:{TEACHER.get_course.name}\n")
        return "".join(data)

    # def add_course(self, course, teacher_id):
    #     pass

    # def remove_course(self, course):
    #     pass

    # @property
    # def list_teachers_with_course(self):
    #     pass


if __name__ == '__main__':
    me = TeachersManager()
    english = Course("english")
    python = Course("python")
    teacher = Teacher("moshe", "m@m.com", english)
    teacher1 = Teacher("david", "a@a.com", python)
    me.add(teacher)
    me.add(teacher1)
    # a = me.get_courses_for_teacher(teacher.get_Id)
    print(me.teachers)