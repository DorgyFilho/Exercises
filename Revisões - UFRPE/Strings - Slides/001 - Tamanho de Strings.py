#1 - Tamanho de Strings

s1 = input('String 1: ')
s2 = input('String 2: ')
tam1 = len(s1)
tam2 = len(s2)

print(f'{s1} --> {tam1} caracteres')
print(f'{s2} --> {tam2} caracteres')

if tam1 > tam2:
    print('Tamanhos Diferentes.')
elif tam1 < tam2:
    print('Tamanhos Diferentes.')
else:
    print('Tamanhos Iguais')

if s1 == s2:
    print('Mesmo Conteúdo!')
else:
    print('Conteúdo Diferente.')

