#144 - Números Primos: While Mode

n = 2
qtdPrimos = 0

while True:
    div = 2
    primo = True
    while div < n:
        if n % div == 0:
            primo = False
            break
        div += 1
    if primo:
        qtdPrimos += 1
        print(n)
    if qtdPrimos == 15:
        break
    n += 1

