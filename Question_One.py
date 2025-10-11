'''Object-Oriented Programming is a way of writing programs by organizing code into 
classes and objects.It focuses on real-world entities like students, cars, or animals,
and represents them as objects with attributes (data) and methods (functions).
For Example:'''
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

Boy1=Student("John",12)
Boy2=Student("Joshua",21)

Boy1.greet()
Boy2.greet()
'''Here:

Student is a class

Each student (like “John”) is an object'''