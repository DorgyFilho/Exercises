#005 - Base e Expoente: Sem Função de Potência

pot = 1
i = 0
b = int(input('Base: '))
k = int(input('Expoente: '))

while i != k:
    pot *= b
    i += 1
print(f'{b} elevado a {i} é {pot}')