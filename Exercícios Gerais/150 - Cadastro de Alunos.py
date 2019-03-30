#150 - Cadastro de Alunos
#Exibir o nome do aluno que tirou a maior nota

alunoMaiorNota = ''
maiorNota = 0
mediaDaTurma = 0
qtdAlunos = 0
soma = 0

for i in range(1,5):
    nome = input('Seu Nome: ')
    nota = float(input('Nota: '))
    soma += nota
    qtdAlunos += 1
    if nota > maiorNota:
        maiorNota = nota
        alunoMaiorNota = nome

    mediaDaTurma = soma/qtdAlunos

print(f'Qtd.Alunos: {qtdAlunos}\nAluno(a) Com a Maior Nota: {alunoMaiorNota}\nMaior Nota: {maiorNota}\nMédia da Turma: {mediaDaTurma:.2f}')
    
    