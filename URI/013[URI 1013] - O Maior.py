#013 - Área

valor = input().split(' ')
a, b, c = valor

maior = (int(a) + int(b) + abs(int(a) - int(b)))/2
res = (int(maior) + int(c) + abs(int(maior) - int(c)))/2

print('%d eh o maior' %res)
