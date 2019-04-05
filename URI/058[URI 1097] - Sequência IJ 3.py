#058 - Sequência IJ 4

I,J,K,L = -1,5,4,3

for i in range(1,6):
    i = I+2
    j = J+2
    k = K+2
    l = L+2
    I = i
    J = j
    K = k
    L = l
    print('I=%d J=%d' %(i,j))
    print('I=%d J=%d' %(i,k))
    print('I=%d J=%d' %(i,l))