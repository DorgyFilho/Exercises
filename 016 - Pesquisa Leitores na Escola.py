#016 - Pesquisa - Leitores na Escola

serie = ''
s1 = 0
s2 = 0
s3 = 0
s4 = 0
maiorLeitor4 = 0
SegNaoGosta = 0
pSerieGosta = 0
while serie != 0:
    serie = int(input('Qual a sua série? 1, 2, 3 ou 4: '))
    if serie == 0:
        print('Programa Encerrado!')
        break
    qtdLivros = int(input('Quantos livros você lê por mês: '))
    gosta = input('Gosta de fazer redação? S ou N: ').upper()
    if serie == 1:
        s1 += 1
        if qtdLivros > 1 and gosta == 'S':
            pSerieGosta += 1
    if serie == 2:
        s2 += 1
        if gosta == 'N':
            SegNaoGosta += 1
    if serie == 3:
        s3 += 1
    if serie == 4:
        s4 += 1
        if qtdLivros > maiorLeitor4:
            maiorLeitor4 = qtdLivros

totalAlunos = s1+s2+s3+s4
if s2 != 0:
    percAlunos2 = (SegNaoGosta/s2)*100.0

print()
print(f'Total de Alunos: {totalAlunos}')
print()
print(f'Quantidade de Alunos na Terceira Série: {s3}')
print()
print(f'Maior quantidade de livros lidos por um aluno da quarta série: {maiorLeitor4}') 
print()
print(f'Percentual de alunos que não gostam de fazer redação e estão na segunda série: {percAlunos2:.2f}')
print()
print(f'Quantidade de alunos que leem mais de um livro por mês e estão na primeira série: {pSerieGosta}')  
print()
print(f'Quantidade de Alunos que estão na segunda série: {s2}')
print()
print(f'Quantidade de Alunos que estão na segunda série e não gosta de fazer redação: {SegNaoGosta}')