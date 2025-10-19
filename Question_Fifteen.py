#super() is used to call methods from the parent class inside the child class.

class Parent:
    def __init__(self, name):
        self.name = name
        print("Parent initialized")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Calls Parent's __init__
        self.age = age
        print("Child initialized")

My_Child = Child("Alice", 12)
