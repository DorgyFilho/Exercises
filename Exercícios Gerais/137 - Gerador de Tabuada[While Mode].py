#137 - Gerador de Tabuada - while Mode

tab = 1
num = 1
while tab <= 10:
    print(f'{tab} x {num} = {tab*num}')
    num += 1
    if num == 11:
        num = 1
        tab += 1
