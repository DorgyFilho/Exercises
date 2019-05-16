#012 - Ausência de Alunos

percMais5 = 0

for i in range(1,15):
    turma = input(f'Nome da {i}° turma: ')
    qtdAlunos = int(input('Quantidade de Alunos: '))
    falta = 0
    presenca = 0
    for k in range(1, qtdAlunos+1):
        mat = input('Matrícula: ')
        chamada = input('F-Faltou ou P-Presente: ').upper()
        if chamada == 'F':
            falta += 1
        else:
            presenca += 1
    
    somaPresFalta = falta + presenca
    mediaPresFalta = (falta*100)/somaPresFalta
    if mediaPresFalta > 5:
        percMais5 += 1
    print(f'A turma {turma} teve {mediaPresFalta}% de alunos faltosos.')

print(f'{percMais5} turma(s) registrou(registraram) mais de 5% das faltas.')
