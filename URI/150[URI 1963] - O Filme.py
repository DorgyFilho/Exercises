#150 - O Filme

def preco():
    a,b = map(float, input().split())
    return a,b

def percentual(a,b):
    Total = a + b
    Diferenca = a - b
    Diferenca = abs(Diferenca)
    Percentual = (Diferenca/a)*100
    Perc = '%.2f' %Percentual
    Final = Perc + '%'
    return Final

def main():
    a,b = preco()
    print(percentual(a,b))

main()