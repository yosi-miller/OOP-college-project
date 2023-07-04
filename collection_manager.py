class CollectionManager:

    def __init__(self):
        self.__collection = []

    @property
    def collection(self):
        return self.__collection

    def amount(self):  # This is get the amount of the collection
        return len(self.__collection)

    def add(self, instance):
        self.collection.append(instance)

    def remove(self, id):
        """
        this is remove instants from the collection
        :param id: the id of the instance that we want to remove
        """
        for instance in self.__collection:
            if instance.Person_Id == id:
                self.__collection.remove(instance)

    def show_all_data(self):
        """This is show all data of the collection"""
        pass