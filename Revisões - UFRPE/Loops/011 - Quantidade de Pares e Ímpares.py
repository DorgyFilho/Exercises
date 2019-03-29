#011 - Quantidade de Pares e Ímpares

qtdPares = 0
qtdImpares = 0
somaPares = 0
somaImpares = 0
for i in range(1,11):
    if i % 2 == 0:
        somaPares += i
        qtdPares += 1
    else:
        somaImpares += i
        qtdImpares += 1

print(f'Soma dos Pares: {somaPares}')
print(f'Soma dos Ímpares: {somaImpares}')
print(f'Quantidade de Pares: {qtdPares}')
print(f'Quantidade de Ímpares: {qtdImpares}')
