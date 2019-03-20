#031 - Calculo
#1. Dois números inteiros e um real
#a. Produto do dobro do primeiro com metade do segundo
#b. Soma do Triplo do Primeiro com o Terceiro
#c. Terceiro Elevado ao Cubo

int1 = int(input('1° Número Inteiro: '))
int2 = int(input('2° Número Inteiro: '))
real = float(input('Número Real: '))

prod = (int1*2)*(int2/2)
somaTriplo = (int1*3) + real
cubo = (real**3)

print(f'Produto: {prod:.2f}\nSoma: {somaTriplo:.2f}\nCubo: {cubo:.2f}')