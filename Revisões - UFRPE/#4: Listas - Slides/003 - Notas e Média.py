#003 - Notas e Média

Notas = []

for i in range(1,5):
    nota = float(input(f'Nota {i}: '))
    Notas.append(nota)

media = sum(Notas)/4

print(f'{Notas} ---> {media:.2f}')
