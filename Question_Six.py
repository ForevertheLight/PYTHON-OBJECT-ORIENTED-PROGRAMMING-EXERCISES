# Attributes are variables that store data inside an object.

# Methods are functions defined inside a class that operate on the object’s data.

class Book:
    def __init__(self, title):
        self.title = title  # attribute

    def read(self):        # method
        print(f"Reading {self.title}")
