#097 - Preenchimento de Vetor IV

#1 - Introdução: Criação de listas correspondentes
#aos números pares e ímpares e, em seguida,
#adicionar os números para as suas respectivas
#listas.

par = []
impar = []
for i in range(15):
    x = int(input(''))
    if x % 2 == 0:
        par.append(x)
    else:
        impar.append(x)

#2 - Desenvolvimento: Verificar as condições de
#impressão dos números e do esvaziamento das
#listas.
    
    if len(par) == 5:
        np = 0
        for j in par:
            print('par[%d] = %d' %(np, j))
            np += 1
        par = []
    
    if len(impar) == 5:
        ni = 0
        for k in impar:
            print('impar[%d] = %d' %(ni, k))
            ni += 1
        impar = []

#3 - Conclusão: Verificar se tem números restantes nas listas
#e imprimi-los, caso tenha.

if len(impar) > 0:
    ni = 0
    for l in impar:
        print('impar[%d] = %d' %(ni, l))
        ni += 1

if len(par) > 0:
    np = 0
    for z in par:
        print('par[%d] = %d' %(np, z))
        np += 1
