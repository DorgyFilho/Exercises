#005 - Quantidade de Espaços e Vogais

espaco = 0
a = 0
e = 0
i = 0
o = 0
u = 0
totVog = 0
frase = input('Frase: ')

for let in frase:
    if ' ' in let:
        espaco += 1
    elif 'a' in let:
        a += 1
    elif 'e' in let:
        e += 1
    elif 'i' in let:
        i += 1
    elif 'o' in let:
        o += 1
    elif 'u' in let:
        u += 1
    
totVog = a+e+i+o+u
print()
print(f'Espaços: {espaco}\nTotal de Vogais: {totVog}')
print()
print(f'a: {a}\ne: {e}\ni: {i}\no: {o}\nu: {u}')