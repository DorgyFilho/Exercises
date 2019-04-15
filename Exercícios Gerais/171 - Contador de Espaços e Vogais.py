#171 - Contador de Espaços e Vogais

frase = input('Frase: ')
espaco = 0
a = 0
e = 0
i = 0
o = 0
u = 0

for k in frase:
    if ' ' in k:
        espaco += 1
    if 'a' in k:
        a += 1
    if 'e' in  k:
        e += 1
    if 'i' in k:
        i += 1
    if 'o' in k:
        o += 1
    if 'u' in k:
        u += 1

print(f'Letra a: {a}')
print(f'Letra e: {e}')
print(f'Letra i: {i}')
print(f'Letra o: {o}')
print(f'Letra u: {u}')
print(f'Espaço: {espaco}')