#005 - Salto Em Distância

Ordem = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto']
resp = 'S'
while resp == 'S':
    Notas = [0.0]*5

    atleta = input('Nome do Atleta: ')
    if atleta != '':
        for i in range(0,5):
            Notas[i] = float(input(f'{Ordem[i]} salto: '))
        media = sum(Notas)/len(Notas)
        print('Resultado Final:')
        print(f'Atleta: {atleta}')
        print(f'Saltos: {Notas[0]} - {Notas[1]} - {Notas[2]} - {Notas[3]} - {Notas[4]}')
        print(f'Média dos Saltos: {media:.2f}')
    else:
        print('Entrada Inválida! Tente novamente.')
        continue
    print('Deseja inserir as notas de outro(a) atleta? - S ou N')
    print()
    resp = input('Resposta: ').upper()
    if resp == 'N':
        print('Encerrado!')
        break
else:
    print('Opção Inválida!')
