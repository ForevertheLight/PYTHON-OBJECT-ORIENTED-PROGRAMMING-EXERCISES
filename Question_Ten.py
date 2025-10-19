#Polymorphism allows different classes to have methods with 
# the same name but different behavior.

class Bird:
    def sound(self):
        print("Chirp")

class Dog:
    def sound(self):
        print("Bark")

for animal in [Bird(), Dog()]:
    animal.sound()  # Same method name, different behavior
