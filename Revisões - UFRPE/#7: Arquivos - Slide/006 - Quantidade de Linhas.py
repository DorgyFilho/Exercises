#006 - Quantidade de Linhas

def Texto():
    with open(input('Digite o endereço de seu texto: ')) as T:
        QP = 0
        for qtd, lin in enumerate(T):
            Qtde = qtd+1
            QP += 1 
    print(f'Quantidade de linhas: {Qtde}')
    print(f'Quantidade de Prints: {QP}')

Texto()