#040 - Números Positivos

positivo = 0
for i in range(6):
    num = float(input(''))
    if num > 0:
        positivo += 1

print('%d valores positivos' %positivo)