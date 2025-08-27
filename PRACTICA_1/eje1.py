class EcuacionLineal:
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def tieneSolucion(self):
        return self.a * self.d - self.b * self.c != 0

    def getX(self):
        numerador = self.e * self.d - self.b * self.f
        denominador = self.a * self.d - self.b * self.c
        return numerador / denominador

    def getY(self):
        numerador = self.a * self.f - self.e * self.c
        denominador = self.a * self.d - self.b * self.c
        return numerador / denominador


def main():
    a, b, c, d, e, f = map(float, input("Ingrese a,b,c,d,e,f: ").split())

    ecuacion = EcuacionLineal(a, b, c, d, e, f)

    if ecuacion.tieneSolucion():
        x = ecuacion.getX()
        y = ecuacion.getY()
        print(f"x = {x}, y = {y}")
    else:
        print("La ecuación no tiene solución")
main()

