#041 - Aumento de Salário

salario = int(input('Salário: '))
percInc = int(input('Percentual de aumento: '))
aumento = (percInc/100)*salario
novoSalario = salario + aumento
print(f'Salário Atual: R${salario:.2f}\nAumento: R${aumento:.2f}\nNovo Salário: R${novoSalario:.2f}')
                    