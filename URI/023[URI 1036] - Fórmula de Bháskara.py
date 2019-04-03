#023 - Fórmula de Bháskara

import math

lin = input('')

linha = lin.split(' ')

a = float(linha[0])
b = float(linha[1])
c = float(linha[2])

try:
    x1 = ((-b) + math.sqrt(math.pow(b,2) - (4*a*c))) / (2*a)
    x2 = ((-b) - math.sqrt(math.pow(b,2) - (4*a*c))) / (2*a)

    print('R1 = %.5f' %x1)
    print('R2 = %.5f' %x2)

except ValueError:
    print('Impossivel calcular')

except ZeroDivisionError:
    print('Impossivel calcular')

#MODO 2

# linha = input().split(' ')

# a = float(linha[0])
# b = float(linha[1])
# c = float(linha[2])
# delta = ((b**2) - 4*a*c)

# if a <= 0 or delta < 0:
#     print('Impossivel calcular')

# else:
#     x1 = (-b + (delta)**0.5)/(2*a)
#     x2 = (-b - (delta)**0.5)/(2*a)

#     print('R1 = %.5f' %x1)
#     print('R2 = %.5f' %x2)