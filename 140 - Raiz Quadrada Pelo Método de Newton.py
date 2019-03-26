#140 - Raíz Quadrada De Um Número Usando o Método de Newton
#Fórmula: p = (b+(n/b))/2
#A cada passo, b=p
#b = 2

n = float(input('Valor a ser calculado: '))
b = 2
p = (b+(n/b))/2
while abs(n-(b*b)) > 0.0001:
    p = (b+(n/b))/2
    b = p
print(f'Raiz Quadrada de {n} é aproximadamente {p}')
    


