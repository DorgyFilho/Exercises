#141 - As Abas de Pericles

N, M = map(int, input().split())
cont = 0

for i in range(M):
    acao = input()
    if acao == 'clicou':
        N -= 1
    if acao == 'fechou':
        N += 1

print(N)

