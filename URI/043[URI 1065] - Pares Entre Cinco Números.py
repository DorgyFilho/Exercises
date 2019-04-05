#043 - Pares Entre Cinco Números

pares = 0
for i in range(5):
    num = int(input(''))
    if num % 2 == 0:
        pares += 1

print('%d valores pares' %pares)
