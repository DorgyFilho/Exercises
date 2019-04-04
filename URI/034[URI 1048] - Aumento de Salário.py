#034 - Aumento de Salário

valor = float(input())
novoSal = 0
if 0.00 <= valor <= 400.00:
    perc = 15
    reajuste = (perc/100)*valor
    novoSal = reajuste + valor
elif 400.00 < valor <= 800.00:
    perc = 12
    reajuste = (perc/100)*valor
    novoSal = reajuste + valor
elif 800.00 < valor <= 1200.00:
    perc = 10
    reajuste = (perc/100)*valor
    novoSal = reajuste + valor
elif 1200.00 < valor <= 2000.00:
    perc = 7
    reajuste = (perc/100)*valor
    novoSal = reajuste + valor
elif valor > 2000.00:
    perc = 4
    reajuste = (perc/100)*valor
    novoSal = reajuste + valor

print('Novo salario: {:.2f}'.format(novoSal))
print('Reajuste ganho: {:.2f}'.format(reajuste))
print('Em percentual: {} %'.format(perc))