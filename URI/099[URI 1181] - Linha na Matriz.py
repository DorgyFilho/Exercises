#099 - Linha na Matriz

#1 - Intro

M = []
soma = 0.0
L = int(input()) #Linha a ser considerada na operação.
R = input() #S ou M?

#2 - Desenvolvimento
for i in range(144): #l x c
    k = float(input())
    M.append(k)

for i in range(12): #144/12 = 12 linhas x 12 Colunas: Trabalho apenas com linhas.
    soma += M[(L*12) + i] #Linha a ser considerada.

if R == 'S':
    print('%.1f' %soma)
if R == 'M':
    print('%.1f' %(soma/12))



