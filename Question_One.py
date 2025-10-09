'''OOP is a programming style where we organize code into classes and objects.
It helps model real-world things (like students, cars, or accounts) 
with data (attributes) and actions (methods).
For Example:'''
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

'''Here:

Student is a class

Each student (like “John”) is an object'''