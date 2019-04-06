#095 - Preenchimento de Vetor II

#Introdução
T = int(input(''))

#Desenvolvimento
K = 0

for i in range(1000):
#Conclusão    
    print('N[%d] = %d' %(i, K))
    K += 1
    if K == T:
        K = 0
    