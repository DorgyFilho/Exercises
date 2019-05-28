#014 - Resto da Divisão Sem Utilizar o Módulo

a = int(input('Dividendo: '))
b = int(input('Divisor: '))
resto = ''
while b <= a:
    a -= b
    resto = a  

print(f'O resto da divisão é {resto}')

"O valor do resto corresponde a quantidade do divisor que resta para alcançar o dividendo."
