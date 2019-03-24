#127 - Competição de Ginástica
Ordem = ['Primeira', 'Segunda', 'Terceira', 'Quarta', 'Quinta', 'Sexta', 'Sétima']

while True:
    notaGin = [0.0]*7

    melhorNota = 0
    piorNota = 0
    media = 0

    atleta = input('Seu Nome: ')

    if atleta != '':
        for s in range(0,7):
            notaGin[s] = float(input(f'{Ordem[s]} nota: '))
        notaGin.sort()
        melhorNota = max(notaGin)
        piorNota = min(notaGin)
        notaGin.remove(melhorNota)
        notaGin.remove(piorNota)
        media = (sum(notaGin))/len(notaGin)

        print('='*50)
        print(f'Melhor Nota ---> {melhorNota}')
        print(f'Pior Nota ---> {piorNota}')
        print(f'Média ---> {media:.2f}')
        print()
        print('Resultado Final')
        print(f'Atleta: {atleta} ---> {media:.2f}')
    else:
        print('Entrada Inválida! Tente novamente.')
    print()
    print('Deseja inserir as notas de outro atleta? - S ou N')
    opcao = input('Resposta: ').upper()
    if opcao == 'N':
        break
