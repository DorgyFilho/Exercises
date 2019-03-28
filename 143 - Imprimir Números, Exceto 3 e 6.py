#143 - Imprimir Números De Um Intervalo - Exceto 3 e 6

n = 6
for i in range(n):
    if i == 3 or i == 6:
        continue
    print(i)