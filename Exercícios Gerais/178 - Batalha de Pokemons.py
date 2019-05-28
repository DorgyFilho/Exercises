#178 - Batalha de Pokemons

nome = []
power = []

while True:
    var = input().replace('\n', '').replace('\r', '')
    if var == 'fimlista':
        break
    var = var.split(':')
    for rose in var:
        if rose.isalpha():
            nome.append(rose)
        elif rose.isdigit():
            power.append(int(rose))

status = zip(nome, power)
Info = dict(status)

while True:
    bat = input().replace('\n', '').replace("\r", '')
    if bat == 'fimbatalhas':
        break
    else:
        bat = bat.split('X')
        p1 = bat[0]
        p2 = bat[1]

    for k in Info.values():
        if Info[p1] > Info[p2]:
            res = p1
        elif Info[p1] < Info[p2]:
            res = p2
        else:
            res = 'empate'
    
    print(res)