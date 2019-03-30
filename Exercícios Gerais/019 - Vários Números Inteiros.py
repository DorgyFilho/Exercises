#019 - Vários Números Inteiros.
#Imprimir o produto dos números pares digitados
#Imprimir a soma dos pares

numero = ''
prodImpar = 1
somaPar = 0
while numero != 9999:
    numero = int(input('Digite um número: '))
    print()
    if numero == 9999:
        print('Programa Encerrado!')
        print()
        break
    if numero % 2 == 0:
        somaPar += numero
    else:
        prodImpar *= numero

print(f'Produto dos Ímpares: {prodImpar}')
print()
print(f'Soma dos Pares: {somaPar}')
