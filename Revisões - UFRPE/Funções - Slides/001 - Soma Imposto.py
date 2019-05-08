#001 - Soma Imposto

def somaImp(custo, taxa):
    Total = (custo*(taxa/100)) + custo
    return f'R$ {Total:.2f}'

custo = float(input('Valor: '))
taxa = float(input('Taxa: '))
Resultado = somaImp(custo, taxa)
print(Resultado)