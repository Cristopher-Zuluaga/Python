from cmath import sqrt


class right_triangle:
    def __init__(self, high, base):
        print("creating the right triangle with side: {d}" .format(d=high))
        print("Base: {d}" .format(d=base))
        self.a = high
        self.b = base
        self.hypotenuse = sqrt((high**2)+(base**2))
    def perimeter(self):
        return self.a+self.b+self.hypotenuse
    def area(self):
        return (self.a*self.b)/2
right_triangle_1 = right_triangle(10,5)
right_triangle_2 = right_triangle(20,7)
right_triangle_3 = right_triangle(70,60)

print("the right_triangle_1 perimeter is: {d}".format(d=right_triangle_1.perimeter()))
print("the right_triangle_2 perimeter is: {d}".format(d=right_triangle_2.perimeter()))
print("the right_triangle_3 perimeter is: {d}".format(d=right_triangle_3.perimeter()))
print("the right_triangle_1 area is: {d}".format(d=right_triangle_1.area()))
print("the right_triangle_2 area is: {d}".format(d=right_triangle_2.area()))
print("the right_triangle_3 area is: {d}".format(d=right_triangle_3.area()))

