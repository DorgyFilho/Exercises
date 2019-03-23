#105 - Idade das Pessoas

n = int(input('Digite a quantidade de participantes da turma: '))
soma = 0
media = 0
for i in range(1, n+1):
    idade = int(input(f'Digite a idade da {i}° pessoa: '))
    soma += idade
    media = soma/i

if 0 <= media <= 25:
    print(f'Turma jovem! Média de idade: {media:.0f} anos')
elif 26 <= media <= 60:
    print(f'Turma adulta! Média de idade: {media:.0f} anos')
else:
    print(f'Turma Idosa! Média de idade: {media:.0f} anos')
