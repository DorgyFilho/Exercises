#004 - Média Aritmética de Três Notas
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))
media = (n1+n2+n3)/3
if not (7.0 <= media <= 10):
    print(f'Reprovado. A média é {media:.2f}')
else:
    print(f'Aprovado com média {media:.2f}')
