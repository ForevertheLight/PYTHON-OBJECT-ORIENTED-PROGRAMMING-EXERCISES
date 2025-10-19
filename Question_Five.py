#self refers to the current instance of the class. It’s used to access variables and methods 
#that belong to the same object.

class Animal:
    def speak(self):
        print("The animal makes a sound.")

    def identify_self(self):
        print(f"This is {self}.")
