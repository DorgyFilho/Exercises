#012 - Listas Derivadas

lista = list(range(16))
L1a9 = []
L3a9 = []
L8a13 = []
L10a15 = []
Pares = []
Impares = []
multi234 = []

for i in lista:
    if i % 2 == 0:
        Pares.append(i)
    if i % 2 != 0:
        Impares.append(i)
    if 1 <= i <= 9:
        L1a9.append(i)
    if 3 <= i <= 9:
        L3a9.append(i)
    if 8 <= i <= 13:
        L8a13.append(i)
    if 10 <= i <= 15:
        L10a15.append(i)
    if i % 2 == 0 and i % 3 == 0 and i % 4 == 0:
        multi234.append(i)

razao = sum(L10a15)/sum(L3a9)

print(lista)
lista.reverse()
print(lista)
print(L1a9)
print(L8a13)
print(L3a9)
print(L10a15)
print(Pares)
print(Impares)
print(f'Razão: {razao:.2f}')
    