#029 - Triângulo

linha = input().split(' ')

A = float(linha[0])
B = float(linha[1])
C = float(linha[2])

somaAB = A+B
somaAC = A+C
somaBC = B+C
perimetro = (A+B+C)
area = ((A+B)*C)/2

if A < somaBC and B < somaAC and C < somaAB:
    print('Perimetro = %.1f' %perimetro)
else:
    print('Area = %.1f' %area)


