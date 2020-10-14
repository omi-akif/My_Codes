class Rectange:
    def __init__(self, length, breadth, unit_cost=0):
        self.length = length
        self.breadth = breadth
        self.unit_cost = unit_cost

    def get_perimeter(self):
        return 2 * (self.length + self.breadth)

    def get_area(self):
        return self.length * self.breadth

    def calculate_cost(self):
        area =  self.get_area()
        return area * self.unit_cost

r = Rectange(10, 50, 2000)

print("Area of the Rectangle: %s cm^2" % (r.get_area()))

print("Cost of the area %s" % (r.calculate_cost()))

class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)

p1 = Person("akif", 25)

p1.myfunc()