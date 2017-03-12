# objetos
import math


class Punto:

    _origen = None

    @staticmethod
    def get_origen():
        if not Punto._origen:
            Punto._origen = Punto()
        return Punto._origen

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, v):
        self._x = v

    @property
    def y(self):
        return self._y

    @x.setter
    def y(self, v):
        self._y = v

    def distancia_origen(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def distancia(self, other):
        a = abs(self.x - other.x)
        b = abs(self.y - other.y)
        return math.sqrt(a ** 2 + b ** 2)

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"


class Linea:
    def __init__(self, x1, y1, x2=None, y2=None):
        if isinstance(x1, Punto):
            self.p1 = x1
            self.p2 = y1
        else:
            self.p1 = Punto(x1, y1)
            self.p2 = Punto(x2, y2)

    @property
    def p1(self):
        return self._p1

    @p1.setter
    def p1(self, v):
        self._p1 = v

    @property
    def p2(self):
        return self._p2

    @p2.setter
    def p2(self, v):
        self._p2 = v

    def __str__(self):
        return str(self.p1) + " - " + str(self.p2)

p1 = Punto(10, 10)
print(p1)

p2 = Punto(20, 20)
print(p2)

l1 = Linea(p1.x, p1.y, p2.x, p2.y)
print(l1)

p3 = Punto(20, 20)
p4 = Punto(30, 30)
l2 = Linea(p3, p4)
print(l2)

#print(Punto.get_origen())
#print(p1.distancia_origen())
#print(p1.distancia(p2))

