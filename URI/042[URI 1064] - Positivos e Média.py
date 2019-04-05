#042 - Positivos e Média

somaPositivo = 0
positivo = 0
for i in range(6):
    num = float(input(''))
    if num > 0:
        somaPositivo += num
        positivo += 1

media = somaPositivo/positivo

print('%d valores positivos' %positivo)
print('%.1f' %media)

