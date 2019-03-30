#119 - Aluno Mais Alto

numAluno = 0
maisAlto = 0
maisBaixo = 1000
alunoAlto = 0
alunoBaixo = 0
qtdeAlunos = int(input('Informe a Quantidade de Alunos: '))

for i in range(1, qtdeAlunos+1):
    cod = int(input(f'Digite o código do {i}° aluno: '))
    altura = int(input(f'Digite a altura do {i}° aluno em cm - Ex: 100cm = 1 metro: '))
    if altura > maisAlto:
        maisAlto = altura
        alunoAlto = cod
    if altura < maisBaixo:
        maisBaixo = altura
        alunoBaixo = cod

print(f'Mais Alto: {alunoAlto} ---> Altura: {maisAlto} cm')
print(f'Mais Baixo: {alunoBaixo}  ---> Altura: {maisBaixo} cm')


