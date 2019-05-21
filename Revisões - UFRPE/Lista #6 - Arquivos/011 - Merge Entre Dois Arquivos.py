#011 - Merge Entre Dois Arquivos

a1 = open(input('Arq: '))
a2 = open(input('Arq 2: '))
mg = open(input('Arquivo Merge: '), 'w')

lin = None
lin2 = None

while True:
    lin1 = a1.readline().replace('\n', '')
    lin2 = a2.readline().replace('\n', '')
    if (lin1 != ''):
        L1 = lin1.split(' ')
        L2 = lin2.split(' ')
        mg.write(L1[0] + ' ')
        mg.write(L2[0] + ' ')
        mg.write(L1[1] + ' ')
        mg.write(L2[1] + ' \n')
    else:
        break

a1.close()
a2.close()
mg.close()