# Instance attributes: Unique to each object.

# Class attributes: Shared by all instances of the class.

class Student:
    school = "ABC College"   # class attribute

    def __init__(self, name):
        self.name = name     # instance attribute

s1 = Student("John")
s2 = Student("Mary")

print(s1.school)  # ABC College
print(s2.school)  # ABC College
