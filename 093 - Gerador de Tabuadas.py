#093 - Gerador de Tabuada

num = int(input('Número a ser multiplicado: '))
multi = int(input('Multiplicador: '))

for i in range(1, multi+1):
    res = num*i
    print(f'{num} x {i} = {res}')
    
