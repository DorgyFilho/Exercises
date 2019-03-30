pares = 0
impares = 0
somaPar = 0
somaImpar = 0
for i in range(1,11):
    num = int(input(f'Digite o {i}° número: '))
    if num % 2 == 0:
        pares += 1
        somaPar += num
    else:
        impares += 1
        somaImpar += num

mediaPar = somaPar/pares
mediaImpar = somaImpar/impares

print(f'Números Pares: {pares}\nNúmeros Ímpares: {impares}\nSoma dos Pares: {somaPar}\nSoma dos ímpares: {somaImpar}\nMédia dos pares: {mediaPar}\nMédia dos Ímpares: {mediaImpar}')

