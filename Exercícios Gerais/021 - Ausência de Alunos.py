#021 - Ausência de Alunos

turmaPercMais5 = 0

for i in range(1,3):
    turma = input(f'Nome da {i}° turma: ').upper()
    qtdAlunos = int(input(f'Quantidade de alunos da {i}° turma: '))
    falta = 0
    presenca = 0
    for j in range(1, qtdAlunos+1):
        mat = input('Matrícula: ')
        resp = input('Faltou ou Presente? F ou P: ').upper()
        if resp == 'F':
            falta += 1
        else:
            presenca += 1

    somaPresFalta = presenca + falta
    mediaPercFalta = (falta*100)/somaPresFalta
    if mediaPercFalta > 5:
        turmaPercMais5 += 1
    print(f'A turma {turma} teve {mediaPercFalta}% de alunos faltosos')

print(f'{turmaPercMais5} turma(s) registrou(registraram) mais de 5% das faltas.')



