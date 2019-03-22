#056 - Leitura de Notas

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))

media = (n1+n2)/2

if media == 10:
    print('Aprovado com distinção!')
elif (7.0 <= media < 10):
    print('Aprovado!')
else:
    print('Reprovado!')