#128 - Número Invertido

num = input('Digite um número: ')
numOriginal = []
Inv = []

for n in num:
    numOriginal.append(n)

tamOrig = len(numOriginal) - 1
k = tamOrig

while tamOrig >= 0:
    Inv.append(numOriginal[tamOrig])
    tamOrig -= 1

NumInv = ''.join(map(str, Inv))

print(f'Número Original: {num} ---> Número Invertido: {NumInv}')
