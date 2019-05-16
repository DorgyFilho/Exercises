#008 - Calcular Salário

nome = input('Nome: ')
sBruto = float(input('Salário Bruto: '))
vDesc = (5/100)*sBruto
sLiq = sBruto - vDesc

print()
print(f'Funcionário(a): {nome}\nSalário Bruto: R${sBruto:.2f}\nValor do Desconto: R${vDesc:.2f}\nSalário Líquido: R${sLiq:.2f}')
