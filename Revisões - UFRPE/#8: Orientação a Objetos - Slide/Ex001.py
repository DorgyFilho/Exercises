#001 - Triângulo

class Triangulo():

    def __init__(self, a, b, c):
        self.ladoA = a
        self.ladoB = b
        self.ladoC = c

    def Perimetro(self):
        soma = self.ladoA + self.ladoB + self.ladoC
        return soma
    
    def MaiorLado(self):
        Maior = self.ladoA
        if self.ladoB > Maior:
            Maior = self.ladoB
        if self.ladoC > Maior:
            Maior = self.ladoC
        return Maior

# a = int(input('Lado A: '))
# b = int(input('Lado B: '))
# c = int(input('Lado C: '))
# Tri = Triangulo(a, b, c)
# print('Perímetro: %d' %Tri.Perimetro())
# print('Maior Lado: %d' %Tri.MaiorLado())