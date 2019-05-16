#002 - É Par Ou Ímpar?

somaPar = 0
somaImpar = 0
qtdPar = 0
qtdImpar = 0

for i in range(1, 11):
    num = int(input(f'Digite o {i}° número: '))
    if num % 2 == 0:
        qtdPar += 1
        somaPar += i
    else:
        qtdImpar += 1
        somaImpar += i

print(f'Qtd. Pares: {qtdPar}\nQtd. Ímpares: {qtdImpar}\nSoma Pares: {somaPar}\nSoma Ímpares: {somaImpar}')