from college import College
from course import Course
from student import Student
from teacher import Teacher
from study_class import StudyClass

# this create a new instance from College class
mivchar = College("mivchar", "bnai brak")

# this create a new instance from Teacher class
barak = Teacher("Barak", "barak@mivchar.com")
avi = Teacher("Avi", "avi@mivchar.com")

# this create a new instance from students class
ushi = Student("Ushi", "ushi@mivchar.com")
yosi = Student("Yosi", "yosi@mivchar,com")

# this create a new instance from Course class
math = Course("math")
english = Course("english")

# this create a new study class
english_class = StudyClass(barak, english)
math_class = StudyClass(avi, math)

# this add a new student to the college
mivchar.studentManger.add(ushi)
mivchar.studentManger.add(yosi)

# this add a new teacher to the college
mivchar.teachersManager.add(barak)
mivchar.teachersManager.add(avi)

# this add a new course to the college
mivchar.coursesManager.add(math)
mivchar.coursesManager.add(english)

# this add a new study class to the college
mivchar.programManager.add(math_class)
mivchar.programManager.add(english_class)

# this add a new student to the study class
math_class.add_student(ushi)
math_class.add_student(yosi)
english_class.add_student(ushi)
english_class.add_student(yosi)

# this add a new grade to the student
math_class.add_grade_to_student(89, ushi.Person_Id)
math_class.add_grade_to_student(86, yosi.Person_Id)
english_class.add_grade_to_student(93, ushi.Person_Id)
english_class.add_grade_to_student(91, yosi.Person_Id)

# print(math_class.show_all_students_class())
# print(english_class.show_all_students_class())

# print(math_class.average_test_students())
# print(english_class.average_test_students())
#
# print(math_class.class_information())
# print(english_class.class_information())

# mivchar.programManager.add(math_class)
# mivchar.programManager.add(english_class)

# print(mivchar.programManager.all_courses_teacher())
