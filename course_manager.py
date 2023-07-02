from collection_manager import CollectionManager
class CourseManager(CollectionManager):

    def add_course(self, instance):
        self.__collection.append(instance)

    def show_information_course(self):
        """
        this is show all data of the course
        :return:
        """
        data = []
        for course in self.__collection:
            data.append(f"Course name: {course.name} , Course id: {course.__id} , Course teacher: {course.__teacher.name}\n")

    def get_teachers_course(self, course):  # הפונקציה מקבלת קורס ומחזירה את המורים שלו
        pass
