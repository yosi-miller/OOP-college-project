class CollectionManager:

    def __init__(self):
        self.__collection = []

    @property
    def collection(self):
        return self.__collection

    def add(self, instance):
        self.__collection.append(instance)

    def remove(self, id):
        """
        this is remove the instants student or __teacher or Instruction
        :param id: the __id of the instance that we want to remove
        """
        for instance in self.__collection:
            if instance.__id == id:
                self.__collection.remove(instance)

    def show_data(self):
        """This is show all data of the students or student or __teacher or Instruction"""
        for student in self.__collection:
            print(f"Student name: {student.name} , Student __id: {student.__id} , Student email: {student.email}")

    @property
    def amount(self):  # This is get the amount of the __teacher or Instruction student
        return len(self.__collection)

    def get_course(self, id):   # איזה קורס יש למורה או לתלמיד (על ידי זיהוי __id)
        pass





