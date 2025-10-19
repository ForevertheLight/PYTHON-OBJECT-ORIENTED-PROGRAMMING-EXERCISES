#Instance methods are functions defined inside a class 
# that operate on the object (using self).

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
