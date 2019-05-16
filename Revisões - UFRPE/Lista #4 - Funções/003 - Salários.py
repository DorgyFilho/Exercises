#003 - Salários

def salario(lista):
    aumento = lambda a: a < 2000
    Resultado = filter(aumento, lista)
    Final = list(Resultado)

    novoSalario = lambda y: y*(20/100) + y
    Result = map(novoSalario, Final)
    Fim = list(Result)
    return Fim

lista = [2500, 2100, 2400, 1950, 1000, 1300, 1999]
result = salario(lista)
print(result)