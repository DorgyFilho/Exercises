#020 - Valor do Seno

x = int(input('X°: '))
n = int(input('n: '))
sen = x
i = 1
exp = 3
num = 0
den = 1
sinal = -1
while i < n:
    num = x**exp
    for k in range(1, exp+1):
        den *= k
    sen += (num/den) * sinal
    sinal *= -1
    exp += 2
    i += 1
    den = 1
print(f'Sen({x}): {sen:.2f}')