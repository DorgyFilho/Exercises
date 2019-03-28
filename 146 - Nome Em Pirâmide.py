#146 - Nome Em Pirâmide

repetir = 'S'
while repetir == 'S':
    nome = input('Nome: ').upper()
    if ' ' in nome:
        print('Digite a string sem espaços')
        continue
    tam = len(nome)

    for i in range(len(nome)):
        espaco = int((tam-i)/2)
        print(' '*espaco+nome[:i+1])

    print()
    print('Deseja repetir a operação? - S/N')
    repetir = input('Resposta: ').upper()
    if repetir == 'N':
        print('Encerrado!')
        break

else:
    print('Operação Inválida!')