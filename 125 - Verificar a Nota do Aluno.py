#125 - Verificar a Nota do Aluno

totAlunos = 0
totNotas = 0
mediaGeral = 0
repetir = 'S'
while repetir == 'S':
    acertos = 0
    for i in range(1,11):
        resp = input(f'Digite a resposta da {i}°Questão: ').upper()
        if i == 1 and resp == 'A':
            acertos += 1
        if i == 2 and resp == 'B':
            acertos += 1
        if i == 3 and resp == 'C':
            acertos += 1
        if i == 4 and resp == 'D':
            acertos += 1
        if i == 5 and resp == 'E':
            acertos += 1
        if i == 6 and resp == 'E':
            acertos += 1
        if i == 7 and resp == 'D':
            acertos += 1
        if i == 8 and resp == 'C':
            acertos += 1
        if i == 9 and resp == 'B':
            acertos += 1
        if i == 10 and resp == 'A':
            acertos += 1
    
    totAlunos += 1
    totNotas += acertos 
    mediaGeral = totNotas/totAlunos

    print()
    print(f'Acertos: {acertos}')
    print(f'Nota: {acertos}')
    print('Há mais alguém para fazer a prova?')
    print()
    repetir = input('Resposta: ').upper()
    if repetir == 'N':
        print('Programa Encerrado!')
        break
else:
    print('Opção Inválida!')
print('GABARITO')
print()
print('1-A\n2-B\n3-C\n4-D\n5-E\n6-E\n7-D\n8-C\n9-B\n10-A')
print()
print(f'{totAlunos} utilizaram o sistema de provas')
print()
print(f'Média Geral: {mediaGeral:.2f}')


    
