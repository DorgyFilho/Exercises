#011 - Calcular Sen(x)

x = int(input('Valor em Graus: '))
n = int(input('Valor de n: '))
sen = x
i = 1
exp = 3
num = 0
den = 1
sinal = -1

while i < n:
    num = i**exp
    for k in range(1, exp+1):
        den *= k
    sen += (num/den) * sinal
    sinal *= -1
    exp += 2
    i += 1
    den = 1
print(f'Sen({x}) = {sen:.2f}')