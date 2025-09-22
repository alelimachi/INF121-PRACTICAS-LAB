import math

class Vec:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
    def __add__(self, v):
        return Vec(self.x + v.x, self.y + v.y, self.z + v.z)

    def esc(self, r):
        return Vec(self.x * r, self.y * r, self.z * r)

    def dot(self, v):
        return self.x * v.x + self.y * v.y + self.z * v.z

    def mag(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    def norm(self):
        m = self.mag()
        if m == 0:
            return Vec(0, 0, 0)
        return Vec(self.x/m, self.y/m, self.z/m)

    def cross(self, v):
        return Vec(self.y*v.z - self.z*v.y,
                   self.z*v.x - self.x*v.z,
                   self.x*v.y - self.y*v.x)
a = Vec(1, 2, 3)
b = Vec(4, 5, 6)

print("a =", a)
print("b =", b)
print("a + b =", a + b)
print("2 * a =", a.esc(2))
print("Longitud de a =", a.mag())
print("Normal de a =", a.norm())
print("Producto escalar ", a.dot(b))
print("Producto vectorial ", a.cross(b))