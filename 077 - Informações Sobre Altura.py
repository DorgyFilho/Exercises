#077 - Conjunto de Dados

menorAltura = 1000
maiorAltura = 0
numHomens = 0
numMulheres = 0
sexoMaisAlta = ''
somaAlturaMulheres = 0

for i in range(1,16):
    sexo = input('Sexo: ').upper()
    altura = float(input('Altura: '))

    if altura > maiorAltura:
        maiorAltura = altura
        sexoMaisAlta = sexo
    
    if altura < menorAltura:
        menorAltura = altura
    
    if sexo == 'M':
        numHomens += 1
    else:
        numMulheres += 1
        somaAlturaMulheres += altura

mediaAltMulheres = somaAlturaMulheres/numMulheres

print(f'Maior Altura: {maiorAltura}')
print(f'Menor Altura: {menorAltura}')
print(f'Número de Homens: {numHomens}')
print(f'Número de Mulheres: {numMulheres}')
print(f'Média da altura das mulheres: {mediaAltMulheres:.2f}')
print(f'Sexo da pessoa mais alta: {sexoMaisAlta}')
    