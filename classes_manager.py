from collection_manager import CollectionManager
from study_class import StudyClass

class ClassesManager(CollectionManager):

    def all_courses_teacher(self):
        """
        return all courses with your teacher
        :return: list of all courses
        """
        result = []
        for data in self.collection:
            result.append(f"the course {data.name} have teacher {data.get_teacher.name}\n")
        return "".join(result)

    def all_grades_student(self):
        results = []
        if len(self.__grade_course_students) > 1:
            for key, value in self.__grade_course_students.items():
                results.append(f"the grade of the course {key} is {value}\n")
            return results
        return "Don't have a grads to the student"

    def all_courses_for_student(self, student_id):
        """
        get all courses for student
        :return: list of all courses
        """
        pass

    def get_teacher_course(self, teacher_id):
        """
        get teacher by course
        :param course:
        :return: teacher
        """
        pass