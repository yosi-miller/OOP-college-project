from collection_manager import CollectionManager
from study_class import StudyClass
from student import Student
from teacher import Teacher
from course import Course

class ProgramManager(CollectionManager):

    def all_courses_teacher(self):
        """
        return all courses with your teacher
        :return: list of all courses
        """
        result = []
        for data in self.collection:
            result.append(f"Course name: {data.course.name}, Teacher name: {data.class_teacher.name}\n")
        return "".join(result)

    def all_grades_student(self, id_student):
        """
        this function return all grades of student
        :param id_student: student_instance.id
        :return: courses and grades
        """
        results = []
        for Class in self.collection:
            if id_student in Class.students_grade:
                results.append(f"{Class.course.name}: {Class.students_grade[id_student]}\n")
        return "".join(results) if results else "Don't have a grade to the student."

    def average_student_courses(self, id_student):
        """
        this function return average from all courses of student
        :param id_student: instance_student.id
        :return:
        """
        results = []
        for Class in self.collection:
            if id_student in Class.students_grade:
                results.append(Class.students_grade[id_student])
        return sum(results) / len(results) if results else "Don't have a grade to the student."

    def all_courses_for_student(self, id_student):
        """
        get all courses for student
        :return: list of all courses
        """
        results = []
        for Class in self.collection:
            if id_student in Class.students:
                results.append(f"{Class.course.name}.\n")
        return "".join(results) if results else "Don't have a courses to the student."

    def get_teacher_courses(self, teacher_id):
        """
        get all courses for teacher
        :param teacher_id: teacher_instance.id
        :return: list of all courses
        """
        result = []
        for Class in self.collection:
            if Class.class_teacher.Person_Id == teacher_id:
                result.append(Class.course.name + "\n")
        return "".join(result) if result else "Don't have a teacher to the course."

    def print_all_students_with_your_courses(self):
        """
        get all students with your courses
        :return: list of all students with your courses
        """
        all_courses = {}
        for Class in self.collection:
            for student in Class.students:
                if student.name not in all_courses:
                    all_courses[student.name] = [Class.course.name]
                else:
                    all_courses[student.name].append(Class.course.name)
        if all_courses:
            for key, value in all_courses.items():
                print(key, ", ".join([str(i) for i in value]), sep=": ")
        else:
            print("Don't have a students with your courses.")

    def show_all_data(self):
        """
        this function show all classes
        :return: all classes
        """
        result = []
        for Class in self.collection:
            result.append(f"Course name: {Class.course.name}, "
                          f"Teacher name: {Class.class_teacher.name},"
                          f"Class id: {Class.Class_Id}\n")
        return "".join(result) if result else "Don't have a classes."


if __name__ == "__main__":
    english = Course("english")
    student1 = Student("avi", "a@a")
    student2 = Student("yosi", "a@a")
    teacher = Teacher("avi", "a@a")

    class1 = StudyClass(teacher, english)

    class1.add_student(student1)
    class1.add_student(student2)

    # class1.add_grade_to_student(100, student1.Id)
    class1.add_grade_to_student(90, student2.Person_Id)

    a = ProgramManager()

    a.add(class1)

    student4 = Student("dudi", "a@a")
    student3 = Student("yamy", "a@a")
    # teacher = Teacher("fadida", "a@a")
    oop = Course("oop")
    class2 = StudyClass(teacher, oop)
    class2.add_student(student1)
    class2.add_student(student2)
    class2.add_grade_to_student(70, student2.Person_Id)

    a.add(class2)
    # for i in a.collection:
    #     print(i.students_grade)
    # print(a.all_courses_teacher())
    # print(a.all_grades_student(student1.Id))
    # print(a.get_teacher_course(teacher.Id))
    # a.print_all_students_with_your_courses()
    # print(a.average_student_courses(student2.Person_Id))
    # print(a.all_courses_for_student(student1.Id))
    print(a.show_all_data())