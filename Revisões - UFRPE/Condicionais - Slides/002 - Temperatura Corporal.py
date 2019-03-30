#002 - Temperatura Corporal

temp = float(input('Digite a temperatura: '))
if temp >= 39:
    print('Febre alta!')
elif temp >= 37 and temp < 39:
    print('Febril!')
else:
    print('Sem Febre!')