#126 - Salto Em Distância

Salto = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto']

while True:
    saltoAtleta = [0.0]*5

    melhorSalto = 0
    piorSalto = 0
    media = 0

    atleta = input('Nome do Atleta: ')

    if atleta != '':
        for s in range(0,5):
            saltoAtleta[s] = float(input(f'{Salto[s]} salto: '))
        saltoAtleta.sort()
        melhorSalto = max(saltoAtleta)
        piorSalto = min(saltoAtleta)
        saltoAtleta.remove(melhorSalto)
        saltoAtleta.remove(piorSalto)
        media = (sum(saltoAtleta))/len(saltoAtleta)

        print('='*50)
        print(f'Melhor Salto ---> {melhorSalto}')
        print(f'Pior Salto ---> {piorSalto}')
        print(f'Média ---> {media:.2f}')
        print('Resultado Final')
        print(f'Atleta: {atleta} ----> {media:.2f}')
    else:
        print('Entrada Inválida! Tente novamente.')
    print()
    print('Deseja inserir outro atleta? - S ou N') 
    opcao = input('Resposta: ').upper()
    if opcao == 'N':
        print('Programa Encerrado.')
        break  

    
