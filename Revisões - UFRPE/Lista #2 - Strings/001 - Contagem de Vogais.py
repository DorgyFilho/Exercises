#001 - Contagem de Vogais

frase = input('Frase: ')
a = 0
e = 0
i = 0
o = 0
u = 0

for k in frase:
    if 'a' in k:
        a += 1
        A = a*'*'
    if 'e' in k:
        e += 1
        E = e*'*'
    if 'i' in k:
        i += 1
        I = i*'*'
    if 'o' in k:
        o += 1
        O = o*'*'
    if 'u' in k:
        u += 1
        U = u*'*'

print(f'a: {A} ---> {a}')
print(f'e: {E} ---> {e}')
print(f'i: {I} ---> {i}')
print(f'o: {O} ---> {o}')
print(f'u: {U} ---> {u}')
