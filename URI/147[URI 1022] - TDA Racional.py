#147 - TDA Racional

def executar():
    K = int(input())

    for k in range(0, K):
        linha = input('')
        op = linha.split(' ')
        N1 = int(op[0])
        D1 = int(op[2])
        sinal = op[3]
        N2 = int(op[4])
        D2 = int(op[6])

        if sinal == '+':
            Num = (N1*D2 + N2*D1)
            Den = (D1*D2)
            MDC = int(calcular(max(Num, Den), min(Num, Den)))
            print(str(Num)+'/'+str(Den) + ' = ' + str(int(Num/MDC))+'/'+str(int(Den/MDC)))   
        elif sinal == '-':    
            Num = (N1*D2 - N2*D1)
            Den = (D1*D2)
            MDC = abs(int(calcular(max(Num, Den), min(Num, Den))))
            print(str(Num)+'/'+str(Den) + ' = ' + str(int(Num/MDC))+'/'+str(int(Den/MDC)))
        elif sinal == '*':    
            Num = (N1*N2)
            Den = (D1*D2)
            MDC = int(calcular(max(Num, Den), min(Num, Den)))
            print(str(Num) +'/'+ str(Den) + ' = ' + str(int(Num/MDC))+'/'+str(int(Den/MDC)))
        elif sinal == '/':
            Num = (N1*D2)
            Den = (N2*D1)
            MDC = int(calcular(max(Num, Den), min(Num, Den)))
            print(str(Num)+'/'+str(Den) + ' = ' + str(int(Num/MDC))+'/'+str(int(Den/MDC)))
    return  

def calcular(N, D):
    R = N%D
    if R == 0:
        return D
    else:
        return calcular(D, R)

executar()
