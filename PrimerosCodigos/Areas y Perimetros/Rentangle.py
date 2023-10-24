class Rectangle:
    def __init__(self, side, base):
        print("creating the square with side: {d}" .format(d=side))
        print("And with base: {d}" .format(d=base))
        self.a = side
        self.b = base
    def perimeter(self):
        return (2*self.a)+(2*self.b)
    def area(self):
        return self.a*self.b
Rectangle_1 = Rectangle(6,3)
Rectangle_2 = Rectangle(4,6)
Rectangle_3 = Rectangle(30,10)

print("the Rectangle_1 perimeter is: {d}".format(d=Rectangle_1.perimeter()))
print("the Rectangle_2 perimeter is: {d}".format(d=Rectangle_2.perimeter()))
print("the Rectangle_3 perimeter is: {d}".format(d=Rectangle_3.perimeter()))
print("the Rectangle_1 area is: {d}".format(d=Rectangle_1.area()))
print("the Rectangle_2 area is: {d}".format(d=Rectangle_2.area()))
print("the Rectangle_3 area is: {d}".format(d=Rectangle_3.area()))

