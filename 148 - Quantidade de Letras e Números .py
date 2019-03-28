#148 - Quantidade de Letras e Números

string = input('Digite a sua string: ').upper()
qtdNum = 0
qtdLet = 0

for i in string:
    if i.isdigit():
        qtdNum += 1
    elif i.isalpha():
        qtdLet += 1
    else:
        print('Inválido!')

print(f'Quantidade de Letras: {qtdLet}\nQuantidade de Números: {qtdNum}')