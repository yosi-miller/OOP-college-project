class Course:
    __Course_Id = 100
    def __init__(self, name: str):
        self.__name = name
        self.__passing_grade = 66
        self.__id = Course.__Course_Id
        Course.__Course_Id += 100

    @property
    def name(self):
        return self.__name

    @property
    def passing_grade(self):
        return self.__passing_grade

    @property
    def Course_Id(self):
        return self.__id