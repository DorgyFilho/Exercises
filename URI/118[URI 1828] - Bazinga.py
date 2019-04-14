#118 - Bazinga!

T = int(input())

for i in range(T):
    S, R = input().split()
    if S == R:
        res = 'De novo!'
    elif S == 'pedra':
        if R == 'tesoura' or R == 'lagarto':
            res = S
        else:
            res = R
    elif S == 'papel':
        if R == 'pedra' or R == 'Spock':
            res = S
        else:
            res = R
    elif S == 'tesoura':
        if R == 'lagarto' or R == 'papel':
            res = S
        else:
            res = R
    elif S == 'lagarto':
        if R == 'Spock' or R == 'papel':
            res = S
        else:
            res = R
    elif S == 'Spock':
        if R == 'tesoura' or R == 'pedra':
            res = S
        else:
            res = R

    if res == S:
        res = 'Bazinga!'
    elif res == R:
        res = 'Raj trapaceou!'

    print('Caso #%d: %s' %(i+1, res))
