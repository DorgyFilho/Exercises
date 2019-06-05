#183 - Retângulo

class Retangulo:

    def __init__(self, a, b):
        self.A = a
        self.B = b
    
    def mostrarLados(self):
        return 'Lado a: %d\nLado b: %d' %(self.A, self.B)
    
    def obterLados(self, A, B):
        self.A = A
        self.B = B
    
    def calcularPerimetro(self):
        return 2*self.A+2*self.B
    
    def calcularArea(self):
        return self.A*self.B
    
    def calcularPiso(self):
        BPiso = 0.45
        APiso = 0.45
        Resultante = BPiso*APiso
        Qtde = self.calcularArea()//Resultante
        return 'Serão necessários %d unidades de piso' %Qtde

Ret = Retangulo(4, 6)
print(Ret.calcularArea())
print(Ret.calcularPiso())
print(Ret.calcularPerimetro())
print(Ret.mostrarLados())

