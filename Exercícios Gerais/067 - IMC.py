#067 - IMC

repetir = 'S'
while repetir == 'S':
    peso = float(input('Peso: '))
    altura = float(input('Altura: '))
    imc = peso/(altura*altura)

    if imc < 20:
        print(f'Abaixo do Peso: {imc:.2f}')
    elif 20 <= imc < 25:
        print(f'Peso Ideal: {imc:.2f}')
    elif 25 <= imc < 30:
        print(f'Sobrepeso: {imc:.2f}')
    elif 30 <= imc < 35:
        print(f'Obesidade Moderada: {imc:.2f}')
    elif 35 <= imc < 40:
        print(f'Obesidade Severa: {imc:.2f}')
    elif 40 <= imc < 50:
        print(f'Obesidade Mórbida: {imc:.2f}')
    else:
        print(f'Super Obesidade: {imc:.2f}')

    print()
    print('Deseja Repetir a Operação? - S ou N')
    repetir = input('Digite a sua resposta: ').upper()
    if repetir == 'N':
        break

print('Programa Encerrado!')