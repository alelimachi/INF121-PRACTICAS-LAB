import random

class Juego:
    def __init__(self, nv):
        self.nv = nv
        self.rec = 0
    
    def reinicia(self):
        self.vid = self.nv
    
    def actrec(self):
        if self.vid > self.rec:
            self.rec = self.vid
    
    def quitav(self):
        self.vid -= 1
        return self.vid > 0


class JuegaNum(Juego):
    def __init__(self, nv):
        super().__init__(nv)
        self.na = 0
    
    def validaNum(self, n):
        return 0 <= n <= 10
    
    def juega(self):
        self.reinicia()
        self.na = random.randint(0, 10)
        print("Adivina un número entre 0 y 10")

        while True:
            n = int(input("Ingresa tu número: "))
            
            if not self.validaNum(n):
                print("Número inválido, intenta de nuevo.")
                continue
            
            if n == self.na:
                print("¡Acertaste!")
                self.actrec()
                break
            else:
                if self.quitav():
                    if n < self.na:
                        print("El número es menor, de nuevo.")
                    else:
                        print("El número es mayor, de nuevo.")
                else:
                    print("No te quedan vidas. El número era:", self.na)
                    break

class JuegaPar(JuegaNum):
    def validaNum(self, n):
        if 0 <= n <= 10 and n % 2 == 0:
            return True
        else:
            print("Error: solo números pares entre 0 y 10.")
            return False

class JuegaImpar(JuegaNum):
    def validaNum(self, n):
        if 0 <= n <= 10 and n % 2 == 1:
            return True
        else:
            print("Error: solo números impares entre 0 y 10.")
            return False
class App:
    @staticmethod
    def main():
        j1 = JuegaNum(3)
        j1.juega()
        j2 = JuegaPar(3)
        j2.juega()
        j3 = JuegaImpar(3)
        j3.juega()

App.main()