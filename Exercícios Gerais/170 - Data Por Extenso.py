#170 - Data Por Extenso

data = input('Data: ')
novaData = data.split('/')
dia = int(novaData[0])
ano = int(novaData[2])

if not (1 <= dia <= 31) or not (ano >= 0):
    print('Inválido!')
else:
    if (1 <= dia <= 31) and novaData[1] == '01' and ano >= 0:
        res = f'Você nasceu em {dia} de Janeiro de {ano}'   
    elif (1 <= dia <= 29) and novaData[1] == '02' and ano >= 0:
        res = f'Você nasceu em {dia} de Fevereiro de {ano}'
    elif (1 <= dia <= 31) and novaData[1] == '03' and ano >= 0:
        res = f'Você nasceu em {dia} de Março de {ano}'
    elif (1 <= dia <= 30) and novaData[1] == '04' and ano >= 0:
        res = f'Você nasceu em {dia} de Abril de {ano}'
    elif (1 <= dia <= 31) and novaData[1] == '05' and ano >= 0:
        res = f'Você nasceu em {dia} de Maio de {ano}'
    elif (1 <= dia <= 30) and novaData[1] == '06' and ano >= 0:
        res = f'Você nasceu em {dia} de Junho de {ano}'
    elif (1 <= dia <= 31) and novaData[1] == '07' and ano >= 0:
        res = f'Você nasceu em {dia} de Julho de {ano}'
    elif (1 <= dia <= 31) and novaData[1] == '08' and ano >= 0:
        res = f'Você nasceu em {dia} de Agosto de {ano}'
    elif (1 <= dia <= 30) and novaData[1] == '09' and ano >= 0:
        res = f'Você nasceu em {dia} de Setembro de {ano}'
    elif (1 <= dia <= 31) and novaData[1] == '10' and ano >= 0:
        res = f'Você nasceu em {dia} de Outubro de {ano}'
    elif (1 <= dia <= 30) and novaData[1] == '11' and ano >= 0:
        res = f'Você nasceu em {dia} de Novembro de {ano}'
    elif (1 <= dia <= 31) and novaData[1] == '12' and ano >= 0:
        res = f'Você nasceu em {dia} de Dezembro de {ano}'
    else:
        res = 'Data Inválida!'
    
    print(res)
