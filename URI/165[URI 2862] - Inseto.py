#165 - Inseto

cases = int(input())
while cases > 0:
    power = int(input())
    if power > 8000:
        print('Mais de 8000!')
    else:
        print('Inseto!')
    cases -= 1