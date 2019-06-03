#019 - Questão Extra 2: Quadrado

class Quadrado:

    def __init__(self, tamLado):
        self.lado = tamLado
    
    def pegaValor(self):
        return self.lado
    
    def novoValor(self, novo):
        self.lado = novo
    
    def calcularArea(self):
        return self.lado**2

Lado = Quadrado(4)
print('Valor lado: %d' %Lado.pegaValor())
print()
print('Área: %d' %Lado.calcularArea())
print()
Lado.novoValor(10)
print('Valor lado: %d' %Lado.pegaValor())
print()
print('Área: %d' %Lado.calcularArea())