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
    
    def juega(self):
        self.reinicia()
        self.na = random.randint(0, 10)
        print("Adivina un número entre 0 y 10")
        
        while True:
            n = int(input("Ingresa tu número: "))
            if n == self.na:
                print("¡Acertaste!")
                self.actrec()
                break
            else:
                if self.quitav():
                    if n < self.na:
                        print("mayor, intenta de nuevo.")
                    else:
                        print("menor, intenta de nuevo.")
                else:
                    print("No te quedan vidas, el número era:", self.na)
                    break
class App:
    @staticmethod
    def main():
        j = JuegaNum(3)  
        j.juega()
App.main()