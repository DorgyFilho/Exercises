#129 - Soma da Série

k = 1
l = 1
k_lista = []
l_lista = []
print('S = ', end='')
while k <= 10 -1:
    print(k,'/',l, '+', end='')
    k_lista.append(k)
    l_lista.append(l)
    k += 1
    l += 2
print(k, '/', l, ' = ', sum(k_lista), '/', sum(l_lista))