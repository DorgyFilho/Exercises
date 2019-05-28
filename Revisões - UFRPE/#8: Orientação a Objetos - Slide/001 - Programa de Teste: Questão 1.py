#001 - Teste da Questão 001

from Ex001 import *

a = int(input('Lado A: '))
b = int(input('Lado B: '))
c = int(input('Lado C: '))
Tri = Triangulo(a, b, c)
print('Perímetro: %d' %Tri.Perimetro())
print('Maior Lado: %d' %Tri.MaiorLado())