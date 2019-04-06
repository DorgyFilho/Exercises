#096 - Preenchimento de Vetor III

#Introdução
N = []
x = float(input(''))
N.append(x)

#Desenvolvimento
for i in range(100):
    x /= 2
    N.append(x)
#Conclusão
    print('N[%d] = %.4f' %(i, N[i]))