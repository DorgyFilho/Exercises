#062 - Temperatura Corporal

temp = float(input('Digite a sua temperatura corporal: '))
if temp >= 39:
    print('Febre Alta')
elif 37 <= temp < 39:
    print('Febril')
else:
    print('Sem Febre')