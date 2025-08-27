import math
class EcuacionCuadratica:
    def __init__(self, a, b, c):  
        self.a = a
        self.b = b
        self.c = c

    def getDiscrim(self):
        return self.b ** 2 - 4 * self.a * self.c

    def getR1(self):
        return (-self.b + math.sqrt(self.getDiscrim())) / (2 * self.a)

    def getR2(self):
        return (-self.b - math.sqrt(self.getDiscrim())) / (2 * self.a)

def main():
    a, b, c = map(float, input("Ingrese a,b,c: ").split())

    ecuacion = EcuacionCuadratica(a, b, c)
    disc = ecuacion.getDiscrim()

    if disc > 0:
        print(f"Las raíces son: r1 = {ecuacion.getR1()}, r2 = {ecuacion.getR2()}")
    elif disc == 0:
        print(f"La raíz única es: r = {ecuacion.getR1()}")
    else:
        print("La ecuación no tiene raíces reales")

main()
