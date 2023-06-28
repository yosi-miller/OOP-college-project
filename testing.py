class MyClass:
    def __init__(self, name):
        self.name = name
        self.instance = []

    def add(self, instance):
        self.instance.append(instance)

    def get_instance(self):
        return self.instance

    def __str__(self):
        class_name = type(self).__name__
        return f"Instance of {class_name}, Name: {self.name}"



a = MyClass("סכ")
a.add(a)
print(a.get_instance())