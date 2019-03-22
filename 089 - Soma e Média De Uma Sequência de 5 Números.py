#089 - Soma e média de uma sequência de 5 números.

soma = 0
media = 0
for i in range(1,6):
    num = int(input(f'Digite o {i}º número: '))
    soma += num
    media = soma/i

print(f'Soma: {soma}\nMédia: {media:.0f}')
