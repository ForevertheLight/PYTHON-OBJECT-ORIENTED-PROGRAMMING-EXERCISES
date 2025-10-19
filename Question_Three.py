#An object is an instance of a class. It represents a specific 
# example of the class with its own data.

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

#Here, Boy1 and Boy2 are the Objects of the class Student.