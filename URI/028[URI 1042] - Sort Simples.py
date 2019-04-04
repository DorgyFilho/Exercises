#028 - Sort Simples

linha = input('').split(' ')

a = int(linha[0])
b = int(linha[1])
c = int(linha[2])

if a < b and a < c:
    n1 = a
    if b < c:
        n2 = b
        n3 = c
    else:
        n2 = c
        n3 = b

elif b < a and b < c:
    n1 = b
    if a < c:
        n2 = a
        n3 = c
    else:
        n2 = c
        n3 = a

elif c < a and c < b:
    n1 = c
    if a < b:
        n2 = a
        n3 = b
    else:
        n2 = b
        n3 = a

print(n1)
print(n2)
print(n3)
print()
print(a)
print(b)
print(c)
