#004 - Número Primo: Modo While

num = 2
qtdPrimos = 0

while True:
    div = 2
    primo = True
    while div < num:
        if num % div == 0:
            primo = False
            break
        div += 1
    if primo:
        print(num)
        qtdPrimos += 1
    if qtdPrimos == 15:
        break
    num += 1