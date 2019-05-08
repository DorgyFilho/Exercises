#129 - Ímpar, Par ou Roubo?

Entrada = input().split()
p = int(Entrada[0])
j1 = int(Entrada[1])
j2 = int(Entrada[2])
r = int(Entrada[3])
a = int(Entrada[4])

Total = j1 + j2

if (Total % 2 == 0 and p == 1) or (Total % 2 == 1 and p == 0):
    Win = '1'
else:
    Win = '2'

if (r == 1 and a == 0) or (r == 0 and a == 1):
    Win = '1'
elif (r == 1 and a == 1):
    Win = '2'

print('Jogador %s ganha!' %Win)
    

    



