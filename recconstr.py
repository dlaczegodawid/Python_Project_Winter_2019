class Rectangle:
    def __init__(self,a=8,b=9):
        self.set_params(a,b)

    def set_params(self, a, b):
        self.a = a
        self.b = b
    def calc_surface(self):
        return self.a*self.b
    def __repr__(self):
        return "Rectangle[" + str(self.a) +"by"+ str(self.b) +"] at " + str(id(self))

r1 = Rectangle(a=4)
r1.b = 10
print(r1.calc_surface())

#Encapsulation
class Rectangle1:
    def __init__(self,__a=8,__b=9):
        self.set_params(__a,__b)

    def set_params(self, __a, __b):
        self.__a = __a
        self.__b = __b
    def calc_surface(self):
        return self.__a*self.__b
    def __repr__(self):
        return "Rectangle[" + str(self.__a) +"by"+ str(self.__b) +"] at " + str(id(self))

r1 = Rectangle(4,5)
r1.__b = 10
print(r1.calc_surface())

#Special functions and operators
