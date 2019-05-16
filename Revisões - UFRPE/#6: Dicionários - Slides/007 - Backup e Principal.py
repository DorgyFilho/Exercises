#007 - Backup e Principal

dPrin = {}
dBack = {}
def imprimir(dic):
    for k, v in dic.items():
        print('%s - %s' %(k,v))

while True:
    cpf = input('Seu CPF: ')
    if cpf.lower() == 'fim':
        break
    nome = input('Nome: ')
    dPrin[cpf] = {'Nome':nome}
    if len(dPrin) == 5:
        imprimir(dPrin)
        dBack.update(dPrin)
        dPrin.clear()

imprimir(dPrin)
imprimir(dBack)


    
        


