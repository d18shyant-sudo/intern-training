#1.Animal Base class
class Animal:
    def speak(self):
        print("The sound of animal")
class Dog(Animal):
    def speak(self):
        print("Bowwww!")
class Cat(Animal):
    def speak(self):
        print("Meowww!")
#2.Shape Base class
class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        super().area()
        print(f"The area of the rectangle is {self.length*self.breadth}")
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        super().area()
        print(f"The area of the circle is {3.14*self.radius*self.radius}")
    def __str__(self):
        return f"This class is used to calculate the area of the circle"
if __name__ == __main__:
    Animals=[Dog(),Cat(),Dog(),Cat(),Dog()]
    for animal in Animals:
        animal.speak()
    r = Rectangle(500,600)
    r.area()
    c = Circle(700)
    c.area()
    print(c)