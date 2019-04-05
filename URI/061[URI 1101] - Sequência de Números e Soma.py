#061 - Sequência de Números e Soma

M = ''
N = ''

while True:
    try:
        valor = input().split()
        M = int(valor[0])
        N = int(valor[1])
        if M < 1 or N < 1:
            break
        
        K = 0    #Variável Temporária

        if M > N:
            K = M
            M = N
            N = K
        
        Soma = 0
        res = ''

        while M <= N:
            res += str(M) + ' '
            Soma += M
            M += 1
        res += 'Sum=%d'
        print(res %Soma)
    
    except:
        break
