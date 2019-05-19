#001 - Escrever Texto

arq = open('/home/dorgyfilho/Documentos/Ex001.txt', 'w')
arq.write(input('Escreva algo: '))
arq.close()

a = open('/home/dorgyfilho/Documentos/Ex001.txt')
cont = a.readlines()
a.close()
for i in cont:
    print(i)