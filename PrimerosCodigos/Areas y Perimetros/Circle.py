class Circle:
    pi = 3.14
    def __init__(self, diameter):
        print("creating the circle with diameter: {d}" .format(d=diameter))
        self.radius = diameter/2
    def circumference(self):
        return 2*Circle.pi*self.radius
    def area(self):
        return Circle.pi*self.radius**2
medium_pizza = Circle(12)
teaching_table= Circle(36)
round_room = Circle(11460)

print("the medium pizza circumference is: {d}".format(d=medium_pizza.circumference()))
print("the teaching_table circumference is: {d}".format(d=teaching_table.circumference()))
print("the round_room circumference is: {d}".format(d=round_room.circumference()))
print("the medium pizza area is: {d}".format(d=medium_pizza.area()))
print("the teaching_table area is: {d}".format(d=teaching_table.area()))
print("the round_room area is: {d}".format(d=round_room.area()))

