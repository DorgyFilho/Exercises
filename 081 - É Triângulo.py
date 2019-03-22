#081 - É Triângulo?

a = int(input('Lado A: '))
b = int(input('Lado B: '))
c = int(input('Lado C: '))
somaAB = a+b
somaBC = b+c
somaAC = a+c

if a <= 0 or b <= 0 or c <= 0:
    print('O triângulo não aceita números negativos ou zero.')

elif c >= somaAB or b >= somaAC or a >= somaBC:
    print('O triângulo não existe.')

elif a == b and a ==c:
    print('Equilátero!')

elif a == b or b == c or c == a:
    print('Isósceles!')

else:
    print('Escaleno!')
    

