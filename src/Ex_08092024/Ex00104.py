# Method Overridding
# says that , child or sub class  can have same name method as the parent or superclass

class Shape:
    def Area(self):
        print("Print the Area of Shape")

class Rectangle(Shape):
    def __init__(self,length, width):
        self.length =  length
        self.width = width

    def Area(self):
        return self.length* self.width

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def Area(self):
        return 3.14*self.radius*self.radius

shape1 = Rectangle(20,30)
print(shape1.Area())

shape2 = Circle(25)
print(shape2.Area())
