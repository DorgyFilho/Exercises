#079 - Números Pares e ímpares

qtdPares = 0
qtdImpares = 0

for i in range(1,12):
    if i % 2 == 0:
        qtdPares += 1
    else:
        qtdImpares += 1
    
print(f'Quantidade de Pares: {qtdPares}')
print(f'Quantidade de Ímpares: {qtdImpares}')