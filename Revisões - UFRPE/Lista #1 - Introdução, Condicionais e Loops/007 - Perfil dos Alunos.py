#007 - Perfil dos Alunos

serie = ''
livrosLidos4serie = 0
maiorLeitor4Serie = 0
naoGostaDeRedacao2 = 0
percNaoGostamRedacao2 = 0
qtdAlunos1MaisDeUmLivro = 0
qtd1Serie = 0
qtd2Serie = 0
qtd3Serie = 0
qtd4Serie = 0

while serie != 0:
    serie = int(input('1.Série, 2.Serie, 3.Serie ou 4.Serie: '))
    if serie <= 0 or serie > 4:
        print('Cadastro Encerrado!')
        break
    else:
        livros = int(input('Quantidade de livros lidos: '))
        gosta = input('Gosta de Redação? S/N: ').upper()
        if gosta != 'S' and gosta != 'N':
            continue
        else:
            if serie == 1:
                qtd1Serie += 1
                if livros > 1 and gosta == 'S':
                    qtdAlunos1MaisDeUmLivro += 1
            if serie == 2:
                qtd2Serie += 1
                if gosta == 'N':
                    naoGostaDeRedacao2 += 1
            if serie == 3:
                qtd3Serie += 1
            if serie == 4:
                qtd4Serie += 1
                if livros > maiorLeitor4Serie:
                    maiorLeitor4Serie = livros

TotalAlunos = qtd1Serie + qtd2Serie + qtd3Serie + qtd4Serie

if qtd2Serie != 0:
    percNaoGostamRedacao2 = (naoGostaDeRedacao2/qtd2Serie)*100

print()
print(f'Total de Alunos: {TotalAlunos}\n1° Série: {qtd1Serie}\n2° Série: {qtd2Serie}\n3° Série: {qtd3Serie}\n4° Série: {qtd4Serie}')
print()
print(f'Maior Quantidade de Livros Lidos na 4°Série: {maiorLeitor4Serie}')
print()
print(f'Percentual de Alunos Que Não Gostam de Redação e Estão Na 2°Série: {percNaoGostamRedacao2:.2f}%')
print()
print(f'Alunos da Primeira Série Que Leem Mais De Um Livro Por Mês e Que Gostam de Redação: {qtdAlunos1MaisDeUmLivro}')
