#104 - Média Aritmética de N notas

num = int(input('Número: '))
media = 0
soma = 0
print()

for i in range(1, num+1):
    nota = float(input(f'{i}º nota: '))
    soma += nota
    media = soma/i
print(f'Soma das notas: {soma:.2f}\nMédia das Notas: {media:.2f}')
