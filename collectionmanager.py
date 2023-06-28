class CollectionManager:
    def __init__(self):
        self.collection = []

    def add(self, instance):
        self.collection.append(instance)

    def get_the_name(self, id):
        for student in self.collection:
            if student.id == id:
                return student.name

    def remove(self, id):
        """
        this is remove the instants student or teacher or Instruction
        :param id: the id of the instance that we want to remove
        """
        for student in self.collection:
            if student.id == id:
                self.collection.remove(student)

    def show_data(self):
        """This is show all data of the students or student or teacher or Instruction"""
        for student in self.collection:
            print(f"Student name: {student.name} , Student id: {student.id} , Student email: {student.email}")

    def get_all_name_instance(self):
        """
        this function return all name of the instance
        :return: list of all name of the instance
        """
        return [instance for instance in self.collection]


    def get_the_amount_of_student(self):  # This is get the amount of the teacher or Instruction student
        pass

    def get_profession_teacher(self, id):   # איזה מקצועות יש למורה או לתלמיד (על ידי זיהוי id)
        pass





