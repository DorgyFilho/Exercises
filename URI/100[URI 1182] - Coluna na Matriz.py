#100 - Coluna na Matriz

#1 - Intro

soma = 0.0
M = []
C = int(input()) #Coluna a ser considerada (0 <= C <= 11)
R = input() #S ou M

#2 - Desenvolvimento
for i in range(144): #l x c = 12 x 12
    k = float(input())
    M.append(k)

for i in range(12): #144/12 = 12 linhas e 12 colunas. Trabalhar com coluna.
    soma += M[C+(i*12)] #Coluna a ser considerada

#3 - Conclusão
if R == 'S':
    print('%.1f' %soma)
if R == 'M':
    print('%.1f' %(soma/12))
