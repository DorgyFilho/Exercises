#031 - Tipos de Triângulos

linha = input().split(' ')
A, B, C = sorted(linha, key=float, reverse=True)
A = float(A)
B = float(B)
C = float(C)

if A >= B+C:
    print('NAO FORMA TRIANGULO')
else:
    if (A**2) == ((B**2) + (C**2)):
        print('TRIANGULO RETANGULO')
    elif (A**2) > ((B**2) + (C**2)):
        print('TRIANGULO OBTUSANGULO')
    elif (A**2) < ((B**2) + (C**2)):
        print('TRIANGULO ACUTANGULO')
    if A == B == C:
        print('TRIANGULO EQUILATERO')
    elif A == B or B == C or A == C:
        print('TRIANGULO ISOSCELES')

