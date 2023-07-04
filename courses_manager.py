from collection_manager import CollectionManager
from course import Course

class CoursesManager(CollectionManager):

    def return_course_by_id(self, course_id):
        """
        get course by id
        :param course_id: instance_course.id
        :return: information about course
        """
        for course in self.collection:
            if course.Course_Id == course_id:
                return f"Course name: {course.name}, Course id: {course.Course_Id}, Course passing grade: {course.passing_grade}"

    def show_all_data(self):
        """
        this function return all information about courses
        :return: list of all courses
        """
        data = []
        if self.collection > 0:
            for COURSE in self.collection:
                data.append(f"Id: {COURSE.Course_Id}, Name: {COURSE.name}\n")
            return "".join(data)
        return "Don't have a courses."