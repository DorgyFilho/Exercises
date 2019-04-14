#125 - De Quem é a Vez?

T = int(input())

for i in range(T):
    Info = input().split()
    j1 = str(Info[0])
    r1 = str(Info[1])
    j2 = str(Info[2])
    r2 = str(Info[3])
    n1, n2 = map(int, input().split())
    res = ''
    total = n1 + n2
    if total % 2 == 0:
        res = 'PAR'
    else:
        res = 'IMPAR'
    
    if r1 == res:
        print(j1)
    elif r2 == res:
        print(j2)
    else:
        print('EMPATE')

