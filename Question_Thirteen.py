#Method overriding occurs when a subclass provides a new 
# version of a method inherited from its parent class.

class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):  # Overriding method
        print("Hello from Child")

My_Child = Child()
My_Child.greet()
