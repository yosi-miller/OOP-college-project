class CollectionManager:

    def __init__(self):
        self.__collection = []

    @property
    def collection(self):
        return self.__collection

    def amount(self):  # This is get the amount of the collection
        return len(self.__collection)

    def add(self, instance):
        self.__collection.append(instance)

    def remove(self, id):
        """
        this is remove instants from the collection
        :param id: the id of the instance that we want to remove
        """
        for instance in self.__collection:
            if instance.__id == id:
                self.__collection.remove(instance)

    def show_data(self):
        """This is show all data of the students or student or __teacher or Instruction"""
        for student in self.__collection:
            print(f"Student name: {student.name} , Student __id: {student.__id} , Student email: {student.email}")