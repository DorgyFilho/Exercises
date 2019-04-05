#054 - Maior e Posição

maiorNumero = 0
posicao = 0

for i in range(1,101):
    num = int(input(''))
    if num > maiorNumero:
        maiorNumero = num
        posicao = i

print(maiorNumero)
print(posicao)