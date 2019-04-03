#009 -  Salário Com Bônus

func = input('')
sFixo = float(input(''))
vendas = float(input(''))
com = (15/100)

bonus = float(vendas*com)
total = sFixo + bonus

print('TOTAL = R$ %.2f' %total)