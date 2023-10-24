class Square:
    def __init__(self, side):
        print("creating the square with side: {d}" .format(d=side))
        self.a=side
    def perimeter(self):
        return self.a+self.a+self.a+self.a
    def area(self):
        return self.a*self.a
square_1 = Square(4)
square_2 = Square(20)
square_3 = Square(100)

print("the square_1 perimeter is: {d}".format(d=square_1.perimeter()))
print("the square_2 perimeter is: {d}".format(d=square_2.perimeter()))
print("the square_3 perimeter is: {d}".format(d=square_3.perimeter()))
print("the square_1 area is: {d}".format(d=square_1.area()))
print("the square_2 area is: {d}".format(d=square_2.area()))
print("the square_3 area is: {d}".format(d=square_3.area()))

