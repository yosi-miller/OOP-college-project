class Course:
    __course_id = 100

    def __init__(self, name):
        self.__name = name
        self.__course_code = Course.__course_id
        Course.__course_id += 100

    @property
    def get_name(self):
        return self.__name

    @property
    def get_course_code(self):
        return self.__course_code

