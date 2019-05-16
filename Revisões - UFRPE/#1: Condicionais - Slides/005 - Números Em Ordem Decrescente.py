#005 - Números Em Ordem Decrescente.

x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))
z = int(input('Digite o terceiro número: '))

if x > y and x > z:
    if y > z:
        print(x,y,z)
    else:
        print(x,z,y)

elif y > x and y > z:
    if x > z:
        print(y,x,z)
    else:
        print(y,z,x)

elif z > x and z > y:
    if x > y:
        print(z,x,y)
    else:
        print(z,y,x)
