#009 - IMC

peso = float(input('Seu Peso: '))
altura = float(input('Sua Altura: '))
imc = peso/(altura*altura)
resultado = ''

if imc < 20:
    resultado = 'Abaixo do Peso'
elif imc >= 20 and imc < 25:
    resultado = 'Peso Ideal'
elif imc >= 25 and imc < 30:
    resultado = 'Sobrepeso'
elif imc >= 30 and imc < 35:
    resultado = 'Obesidade Moderada'
elif imc >= 35 and imc < 40:
    resultado = 'Obesidade Severa'
elif imc >= 40 and imc < 50:
    resultado = 'Obesidade Mórbida'
else:
    resultado = 'Super Obesidade' 

print(f'Seu IMC: {imc:.2f}\nResultado: {resultado}')
