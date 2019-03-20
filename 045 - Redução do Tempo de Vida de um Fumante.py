#045 - Redução do tempo de vida de um fumante

cigDia = int(input('Quantidade de cigarros consumida no dia: '))
anosFumante = float(input('Há quanto tempo, em anos, você fuma?: '))
reduzMin = anosFumante*365*cigDia*10 #10 minutos = 1/6 hora.
reduzDias = reduzMin/(24*60) #24 horas por dia e 60 minutos por hora
print(f'Redução do tempo de vida em dias: {round(reduzDias)} dias') 
