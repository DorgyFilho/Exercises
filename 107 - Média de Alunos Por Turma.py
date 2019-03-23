#107 - Média de Alunos Por Turma

turma = int(input('Digite a quantidade de turmas: '))
media = 0
soma = 0

for i in range(1, turma+1):
    alunos = int(input(f'Quantidade de Alunos na {i}° Turma: '))
    soma += alunos
    media = soma/i

print(f'A Escola Possui {turma} turmas\nMédia de Alunos Por Turma: {media:.0f}')
