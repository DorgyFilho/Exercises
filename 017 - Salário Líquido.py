#017 - Salário Líquido

nome = input('Seu Nome: ')
sBruto = int(input('Seu Salário: R$'))
imposto = (5/100)
desconto = sBruto*imposto
sLiq = sBruto - desconto

print()
print(f'Nome: {nome}')
print()
print(f'Salário Bruto: R${sBruto:.2f}')
print()
print(f'Valor do Desconto: R${desconto:.2f}')
print()
print(f'Salário Líquido: R${sLiq:.2f}')
