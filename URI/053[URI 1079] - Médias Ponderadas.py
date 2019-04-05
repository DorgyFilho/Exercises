#053 - Médias Ponderadas

N = int(input(''))
soma = 0
media = 0

for i in range(N):
    valor = input().split()
    n1 = float(valor[0])*2
    n2 = float(valor[1])*3
    n3 = float(valor[2])*5

    soma = n1+n2+n3

    media = soma/10

    print('%.1f' %media)




    
