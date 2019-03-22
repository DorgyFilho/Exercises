#070 - Quantidade Indeterminada de Números

num = ''
numImpar = ''
while num != 99:
    num = int(input('Digite um número: '))
    if num == 99:
        print('Programa Encerrado!')
        break
    if num % 2 != 0:
        num = str(num)+' '
        numImpar += num
        print(numImpar)
        print()
        continue
    