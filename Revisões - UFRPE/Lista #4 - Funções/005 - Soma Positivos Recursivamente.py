#005 - Soma de Positivos de Maneira Recursiva

def Soma(lista):
    positivos = lambda a: a > 0
    Result = filter(positivos, lista)
    Fim = list(Result)

    Total = 0
    if len(Fim) > 0:
        Total += Fim[0] + Soma(Fim[1:])
    return Total

lista = [-4, 1, 3, -7, 12, 8, 6, -2, 20]
Final = Soma(lista)
print(Final)