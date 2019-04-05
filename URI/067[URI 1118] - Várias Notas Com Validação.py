#067 - Várias Notas Com Validação

resp = 's'
while resp == 's':
    cont = 0
    media = 0
    op = 3
    while cont < 2:
        nota = float(input())
        if nota >= 0 and nota <= 10:
            media += nota
            cont += 1
        else:
            print('nota invalida')
    print('media = %.2f' %(media/2))

    while op != 1 and op != 2:
        op = int(input('novo calculo (1-sim 2-nao)\n'))
        if op == 1:
            resp = 's'
        elif op == 2:
            resp = 'n' 
        else:
            op = int(input('novo calculo (1-sim 2-nao)\n'))



    
