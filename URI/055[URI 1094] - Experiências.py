#055 - Experiências

N = int(input(''))
R = 0
C = 0
S = 0
total = 0

for i in range(1,N+1):
    valor = input().split()
    qtd = int(valor[0])
    tipo = valor[1]
    if tipo == 'R':
        R += qtd
    elif tipo == 'C':
        C += qtd
    elif tipo == 'S':
        S += qtd
    total += qtd
    percRato = (R/total)*100
    percCoelho = (C/total)*100
    percSapo = (S/total)*100

print('Total: %d cobaias' %total)
print('Total de coelhos: %d' %C)
print('Total de ratos: %d' %R)
print('Total de sapos: %d' %S)
print('Percentual de coelhos: {:.2f} %'.format(percCoelho))
print('Percentual de ratos: {:.2f} %'.format(percRato))
print('Percentual de sapos: {:.2f} %'.format(percSapo))
