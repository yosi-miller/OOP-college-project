from person_class import Person

class Student(Person):

    def __init__(self, name, email, instructor):
        Person.__init__(self, name, email)
        self.teacher = []
        self.instructor_name = instructor
        self.profession = []

    def add_teacher(self, teacher): #הוספת מורה
        self.teacher.append(teacher)

    def remove_teacher(self, teacher):#הסרת מורה
        self.teacher.remove(teacher)

    def add_profession(self, profession): #הוספת מקצוע
        self.profession.append(profession)

    def remove_profession(self, profession):#הסרת מקצוע
        self.profession.remove(profession)

    def switch_instructor(self, instructor):  # שינוי מתרגל/מדריך
        self.instructor_name = instructor
