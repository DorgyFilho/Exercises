#010 - Interrogatório Policial

perguntas = ['Telefonou Para a Vítima?', 'Esteve no Local do Crime?',
'Mora Perto da Vítima?', 'Tinha Dívidas Com a Vítima?', 'Já Trabalhou Com a Vítima?']

positivo = 0

for i in range(len(perguntas)):
    print(perguntas[i])
    resp = input('Resposta - S ou N: ').upper()

    if resp == 'S':
        positivo += 1

if positivo == 2:
    print('Suspeito(a)')
elif 2 < positivo < 5:
    print('Cúmplice!')
elif positivo == 5:
    print('Assassino(a)!')
else:
    print('Inocente!')