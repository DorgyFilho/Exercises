#033 - Rendimento do Trabalho

pesoPermitido = 50
peso = int(input('Peso: '))
if peso > pesoPermitido:
    excesso = peso - pesoPermitido
    multa = 4*excesso
    print(f'Peso Obtido: {peso}kg\nExcesso de Peso: {excesso}kg\nMulta a Pagar: R${multa:.2f}')
else:
    print('Você está isento.')
