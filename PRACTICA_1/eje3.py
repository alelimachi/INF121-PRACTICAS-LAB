class Estadisticas:
    def __init__(self, valores): 
        self.valores = valores 

    def promedio(self):
 
        return sum(self.valores) / len(self.valores)

    def desviacion(self, promedio):
        varianza = sum([(x - promedio) ** 2 for x in self.valores]) / (len(self.valores) - 1)
        return varianza ** 0.5
    
class Main:
    def __init__(self):  
        self.valores = []

    def ingresar_valores(self):
        self.valores = list(map(float, input().split()))

    def mostrar_resultados(self):
        estadisticas = Estadisticas(self.valores)

        prom = estadisticas.promedio()
        
        desv = estadisticas.desviacion(prom)
        
        print(f"El promedio es: {prom:.2f}")
        print(f"La desviación estándar es: {desv:.5f}")

programa = Main()
programa.ingresar_valores()
programa.mostrar_resultados()
