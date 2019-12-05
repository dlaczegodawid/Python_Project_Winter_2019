
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, a=8, b=9):
        self.set_params(a, b)

    def set_params(self, a, b):
        self._a = a
        self._b = b

    def get_a(self):
        return self._a

    def get_b(self):
        return self._b

    def __repr__(self):
        return self.__class__.__name__ + "[" + str(self._a) + " by " + str(self._b) + "] at " + str(hex(id(self)))

class Rectangle(Shape):
    def calc_surface(self):
        return self._a * self._b


import math
class Cycle(Shape):
    def __init__(self,a):
        super().__init__(a,0)
        #self._a=a

    def calc_surface(self):
        return math.pi*self._a**2
    def __repr__(self):
        return self.__class__.__name__ + "[r=" + str(self._a) + "] at " + str(hex(id(self)))
c = Cycle(3)
print(c.calc_surface())
print(c)

class Square(Rectangle):
    def __init__(self,a):
        super().__init__(a,a)

s1 = Square(4)
print(s1)
print(s1.calc_surface())





#r1 = Rectangle(4, 6)
#s = Shape(2,2)
#print(r1)
#print(s)
#print(r1.calc_surface())
#print(r1.get_a())
#print(r1.get_b())

#class HybridShape(Rectangle, Cycle):
#    pass

#h1 = Rectangle(4,6)
#print(h1)
#print(h1.calc_surface())

#square inherit from rectangle we only set a then te rectangle

#create two triangle
#dowonly trojkat
#trojkat rownoboczny
#obwod