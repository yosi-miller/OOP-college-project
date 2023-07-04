class Course:

    def __init__(self, name: str):
        self.__name = name
        self.__passing_grade = 66

    @property
    def name(self):
        return self.__name

    @property
    def passing_grade(self):
        return self.__passing_grade