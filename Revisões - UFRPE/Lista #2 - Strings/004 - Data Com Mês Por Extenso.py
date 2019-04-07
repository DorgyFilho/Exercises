data = input('Informe a data no formato DD/MM/AAAA: ')
novaData = data.split('/')
dia = int(novaData[0])
ano = int(novaData[2])
res = ''

if (dia > 0 and dia <= 31) and novaData[1] == '01' and ano >= 0:
    res = f'Você nasceu no dia {dia} de Janeiro de {ano}'
    print(res)
elif (dia > 0 and dia <= 28) and novaData[1] == '02' and ano >= 0:
    res = f'Você nasceu no dia {dia} de Fevereiro de {ano}'
    print(res)
elif (dia > 0 and dia <= 31) and novaData[1] == '03' and ano >= 0:
    res = f'Você nasceu no dia {dia} de Março de {ano}'
    print(res)
elif (dia > 0 and dia <= 30) and novaData[1] == '04' and ano >= 0:
    res = f'Você nasceu no dia {dia} de Abril de {ano}'
    print(res)
elif (dia > 0 and dia <= 31) and novaData[1] == '05' and ano >= 0:
    res = f'Você nasceu no dia {dia} de Maio de {ano}'
    print(res)
elif (dia > 0 and dia <= 30) and novaData[1] == '06' and ano >= 0:
    res = f'Você nasceu no dia {dia} de Junho de {ano}'
    print(res)
elif (dia > 0 and dia <= 31) and novaData[1] == '07' and ano >= 0:
    res = f'Você nasceu no dia {dia} de Julho de {ano}'
    print(res)
elif (dia > 0 and dia <= 31) and novaData[1] == '08' and ano >= 0:
    res = f'Você nasceu no dia {dia} de Agosto de {ano}'
    print(res)
elif (dia > 0 and dia <= 30) and novaData[1] == '09' and ano >= 0:
    res = f'Você nasceu no dia {dia} de Setembro de {ano}'
    print(res)
elif (dia > 0 and dia <= 31) and novaData[1] == '10' and ano >= 0:
    res = f'Você nasceu no dia {dia} de Outubro de {ano}'
    print(res)
elif (dia > 0 and dia <= 30) and novaData[1] == '11' and ano >= 0:
    res = f'Você nasceu no dia {dia} de Novembro de {ano}'
    print(res)
elif (dia > 0 and dia <= 31) and novaData[1] == '12' and ano >= 0:
    res = f'Você nasceu no dia {dia} de Dezembro de {ano}'
    print(res)
else:
    res = 'Data Inválida'
    print(res)
