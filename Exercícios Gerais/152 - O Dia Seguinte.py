#152 - O Dia Seguinte

#1 - Ano
bissexto = ''
ano = int(input('Ano: '))

if ano % 400 == 0:
    bissexto = True
elif ano % 100 == 0:
    bissexto = False
elif ano % 4 == 0:
    bissexto = True
else:
    bissexto = False

#2 - Mês
mes = int(input('Digite o mês[1-12]: '))

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    diasMes = 31
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    diasMes = 30
elif mes == 2:
    diasMes = 29
elif mes == 2 and bissexto == True:
    diasMes = 29
elif mes == 2 and bissexto == False:
    diasMes = 28

#3 - Dia
dia = int(input('Digite o dia[1-31]: '))

if dia < diasMes:
    dia += 1
else:
    dia = 1
    if mes == 12:
        dia = 1
        ano += 1
    else:
        mes += 1

#4 - Resultado
print(f'Amanhã será dia {dia}/{mes}/{ano}') 