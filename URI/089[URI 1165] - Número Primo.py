#089 - Número Primo

N = int(input())

for k in range(N):
    X = int(input())
    primo = True

    for i in range(2, X):
        if X%i == 0:
            primo = False
            break
    
    if primo:
        print('%d eh primo' %X)
    else:
        print('%d nao eh primo' %X)

