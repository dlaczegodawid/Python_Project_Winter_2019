#Please use the latest(Shapes_abstract) structures and extend it by:
#1. adding a Triangle and EquilateralTriangle
#2. adding perimeter calculation to every structure
#3. adding a Square that inherits from Rectangle and uses its calc_surface implementation
#4. providing some code that tests the newfunctionality and structures

import math

from abc import ABC, abstractmethod
class Shape(ABC):
    def __init__(self, a=8, b=9):
        self.set_params(a, b)

    @abstractmethod
    def calc_surface(self):
        pass
    @abstractmethod
    def calc_perim(self):
        pass

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
    def calc_perim(self):
        return 2*self._a+2*self._b
r1 = Rectangle(5,2)
print(r1)
print(r1.calc_surface())
print(r1.calc_perim())

class Circle(Shape):
    def __init__(self, a):
        # call constructor from super class (Shape)
        super().__init__(a, 0)
        #self._a = a

    def calc_surface(self):
        return math.pi*self._a**2

    def calc_perim(self):
        return 2*math.pi*self._a

    def __repr__(self):
        return self.__class__.__name__ + "[r=" + str(self._a) + "] at " + str(hex(id(self)))
c1 = Circle(6)
print(c1)
print(c1.calc_surface())
print(c1.calc_perim())

class Square(Rectangle):
    def __init__(self,a):
        super().__init__(a,a)

s1 = Square(3)
print(s1)
print(s1.calc_surface())
print(s1.calc_perim())

class Triangle(Shape):
    def __init__(self,a,b,c):
        Shape.__init__(self, a, b)
#       super(Triangle,self).__init__(a,b)
        self._c = c

    def if_triangle(self):
        if (self._a + self._b <= self._c) or (self._a + self._c <= self._b) or (self._b + self._c <= self._a):
            return False
        else:
            return True
    def __repr__(self):
        if self.if_triangle():
            return self.__class__.__name__ + " [" + str(self._a) + " - " + str(self._b) + " - " + str(self._c) + "] at " + str(hex(id(self)))
        else:
            return "Cannot Construct Triangle " + " [" + str(self._a) + " - " + str(self._b) + " - " + str(self._c) + "] at " + str(hex(id(self)))

    def calc_surface(self):

        if self.if_triangle():
            s = (self._a + self._b + self._c) / 2
            return (s*(s-self._a)*(s-self._b)*(s-self._c)) ** 0.5
        else:
            return "not a triangle - cannot calculate surface"

    def calc_perim(self):
        if self.if_triangle():
            return self._a+self._b+self._c
        else:
            return "not a triangle - cannot calculate perimeter"
t1 = Triangle(5,4,6)
print(t1)
print(t1.calc_surface())
print(t1.calc_perim())

t3 = Triangle(2,2,10)
print(t3)
print(t3.calc_surface())
print(t3.calc_perim())

class EquilateralTriangle(Triangle):
    def __init__(self,a):
        super().__init__(a,a,a)


t2 = EquilateralTriangle(2)
print(t2)
print(t2.calc_surface())
print(t2.calc_perim())