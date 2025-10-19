#Inheritance allows a class (child/subclass) to inherit attributes 
# and methods from another class (parent/superclass).

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.speak()
dog.bark()
