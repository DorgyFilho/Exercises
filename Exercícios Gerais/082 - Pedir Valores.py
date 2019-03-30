#082 - Pedir valores

while True:
    nota = int(input('Digite uma nota: '))
    if nota < 0 or nota > 10:
        print('Valor Inválido')
        continue
    else:
        print(f'Sua nota foi {nota}')
        break
