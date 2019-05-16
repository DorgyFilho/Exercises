#143 - Etiquetas de Noel

dicio = {}
n = int(input())
while n > 0:
    n -= 1
    lingua = input()
    traducao = input()
    dicio[lingua] = traducao

m = int(input())
while m > 0:
    m -= 1
    nome = input()
    lingua = input()
    resultado = dicio[lingua]
    print(nome)
    print(resultado)
    print()