#TASK 5
import math
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def equality(self, other):
        return self.x == other.x and self.y == other.y
    def  __str__(self):
        return f'({self.x}, {self.y})'
    def euc_dist(self, other):
        return math.sqrt((other.x-self.x)**2 + (other.y-self.y)**2)
    
class Vector(Point):
    def __init__(self,x,y):
        super().__init__(x, y)
    def __str__(self):
        return f'⟨{self.x}, {self.y}⟩'
    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y)
    
point1 = Point(2,9)
point2 = Point(-6,10)
vector1 = Vector(3,5)
vector2 = Vector(0,-6)

print(point1)
print(point2)
print(point1.equality(point2))
print(point1.equality(point1))
print(point1.euc_dist(point2))

print(vector1)
print(vector1+vector2)

    
