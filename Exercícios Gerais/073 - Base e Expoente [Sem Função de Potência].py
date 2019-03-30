#073 - Base e Expoente - Sem função de Potência

pot = 1
i = 0
base = int(input('Base: '))
exp = int(input('Expoente: '))
while i != exp:
    pot *= base
    i += 1
print(f'{base} elevado à {i} = {pot}')