#006 - Aumento de Salário

salario = float(input('Meu salário: '))
aumento = (20/100)*salario
novoSalario = salario + aumento
print(f'O novo salário passou de R${salario:.2f} para R${novoSalario:.2f}')
