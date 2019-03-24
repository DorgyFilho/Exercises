#130 - Soma da Série V2

h = 1
n = 2
hLista = []
nLista = []
print('H = 1 +', end='')
while n <= 10 -1:
    print(' ',h, '/', n, ' + ', end='')
    hLista.append(h)
    nLista.append(n)
    n += 1
print(h, '/', n, '=>', sum(hLista), '/', sum(nLista), '=>', round(sum(hLista)/sum(nLista)), 2)
