#005 - Par e Ímpar

Par = []
Impar = []
lista = list(range(1,21))

for i in lista:
    if i % 2 == 0:
        Par.append(i)
    else:
        Impar.append(i)

print(Impar)
print(Par)