#035 - Notas Bimestrais e Média

total = 0
for i in range(1,5):
    nota = float(input(f'Digite a {i}° nota: '))
    total += nota

media = total/4

if media == 10:
    print('Aprovado com louvor!')
elif 7.0 <= media < 10:
    print(f'Aprovado com média {media:.2f}!')
else:
    print(f'Reprovado com média {media:.2f}.')