#007 - Jo Ken Po

def JKP(p1, p2):
    if p1 == 'pedra' and p2 == 'tesoura':
        res = 'P1 é o vencedor!'
        return res
    elif p1 == 'papel' and p2 == 'pedra':
        res = 'P1 é o vencedor!'
        return res
    elif p1 == 'tesoura' and p2 == 'papel':
        res = 'P1 é o vencedor!'
        return res
    elif p2 == 'pedra' and p1 == 'tesoura':
        res = 'P2 é o vencedor!'
        return res
    elif p2 == 'papel' and p1 == 'pedra':
        res = 'P2 é o vencedor!'
        return res
    elif p2 == 'tesoura' and p1 == 'papel':
        res = 'P2 é o vencedor!'
        return res
    elif p1 == p2:
        res = 'Empate!'
        return res
    else:
        return False

p1 = input('Opção J1: ').lower()
p2 = input('Opção J2: ').lower()
print(JKP(p1, p2))