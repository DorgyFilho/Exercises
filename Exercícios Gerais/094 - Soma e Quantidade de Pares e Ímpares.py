#094 - Soma de Pares e ímpares

somaPar = 0
somaImpar = 0
qtdPar = 0
qtdImpar = 0
inicio = int(input('Número Inicial: '))
fim = int(input('Número Final: '))

for i in range(inicio, fim+1):
    if i % 2 == 0:
        qtdPar += 1
        somaPar += i
    else:
        qtdImpar += 1
        somaImpar += i

print(f'Qtd Pares: {qtdPar}\nQtd Ímpares: {qtdImpar}\nSoma Pares: {somaPar}\nSoma Ímpares: {somaImpar}')
