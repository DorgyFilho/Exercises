#021 - Exercício Extra 4: Retângulo

class Retangulo:

    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB
    
    def mudarValor(self, a, b):
        self.ladoA = a
        self.ladoB = b
    
    def retornarLados(self):
        return ('Lado a: %d / Lado b: %d' %(self.ladoA, self.ladoB))
    
    def calculaPerimetro(self):
        return 2*self.ladoA + 2*self.ladoB
    
    def calculaArea(self):
        return self.ladoA * self.ladoB

Ret = Retangulo(4,5)
print(Ret.retornarLados())
print()
print(Ret.calculaPerimetro())
print()
print(Ret.calculaArea())
print()
Ret.mudarValor(10,10)
print(Ret.retornarLados())
print()
print(Ret.calculaPerimetro())
print()
print(Ret.calculaArea())