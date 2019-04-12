#007 - Intercalando Elementos de Duas Listas

L1 = [1,2,3]
L2 = ['a','b','c','d','e']

Intercalada = []

for i,j in zip(L1, L2):
    Intercalada.append(i)
    Intercalada.append(j)
Intercalada.extend(['d', 'e'])
print(Intercalada)