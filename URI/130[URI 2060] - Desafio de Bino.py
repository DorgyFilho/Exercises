#130 - Desafio de Bino

L = int(input())
N = input().split()

Cont2 = 0
Cont3 = 0
Cont4 = 0
Cont5 = 0
for i in range(L):

    if (int(N[i]) % 2 == 0):
        Cont2 += 1
    if (int(N[i]) % 3 == 0):
        Cont3 += 1
    if (int(N[i]) % 4 == 0):
        Cont4 += 1
    if (int(N[i]) % 5 == 0):
        Cont5 += 1

print('%d Multiplo(s) de 2' %Cont2)
print('%d Multiplo(s) de 3' %Cont3)
print('%d Multiplo(s) de 4' %Cont4)
print('%d Multiplo(s) de 5' %Cont5)