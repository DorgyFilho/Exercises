#001 Imposto

def somaImposto(custo, taxa):
    imposto = (taxa/100)*custo
    resultado = custo + imposto
    return resultado

custo = float(input('Valor: '))
taxa = float(input('Taxa: '))
Total = somaImposto(custo, taxa)
print(f'{Total:.2f}')