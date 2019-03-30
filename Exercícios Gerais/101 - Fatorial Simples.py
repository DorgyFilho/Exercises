#101 - Fatorial Simples

n = int(input('Digite um número para calcular o fatorial: '))
fat = 1
for i in range(0,n):
    fat *= (n-i)
print(f'O fatorial de {n} é {fat}')
