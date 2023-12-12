# 10. WAP to define a class Point with coordinates x and y as attributes. Create relevant methods and print the objects. Also define a method distance to calculate the distance between any two point objects.

import math

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def display(self):
        print(f"Point({self.x}, {self.y})")

    def distance(self, other_points):
        distance = math.sqrt((self.x-other_points.x)**2 + (self.y - other_points.y)**2)
        return distance

point1 = Point(3,4)
point2 = Point(6,8)

point1.display()
point2.display()
distance = point1.distance(point2)
print("The distance between Point({}, {}) and Point({}, {}) is: {}".format(point1.x,point1.y,point2.x,point2.y,distance))
