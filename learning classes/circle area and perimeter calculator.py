class Circle:
    def __init__(self,radius):
        self.radius = radius

    def circle_area(self):
        self.radius = int(self.radius)
        area = 3.14 * self.radius**2
        print(area)

    def circle_perimeter(self):
        self.radius = int(self.radius)
        perimeter = 2 * 3.14 * self.radius
        print(perimeter)


def take_input():
    while True:
        print("Enter q anytime to quit")
        radii = str(input("Enter radius of circle:"))
        if radii == "q":
            break
        circle = Circle(radii)
        circle.circle_area()
        circle.circle_perimeter()

take_input()