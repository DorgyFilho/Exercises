#160 - Diamante

k = int(input('Tamanho da Pirâmide: '))

for i in range(k-1):
    print((k-i)*' '+(2*i+1)*'*')
for i in range(k-1,-1,-1):
    print((k-i)*' '+(2*i+1)*'*')