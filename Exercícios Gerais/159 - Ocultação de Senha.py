#159 - Ocultação de Senha
#Use o Programa 158 Como Base

import re

senha = input('Digite Sua Senha: ')
Word = True

while Word:
    if len(senha) < 4 or len(senha) > 20:
        break
    elif not re.search('[a-z]', senha):
        break
    elif not re.search('[0-9]', senha):
        break
    elif not re.search('[A-Z]', senha):
        break
    elif not re.search('[$#@]', senha):
        break
    elif re.search('\s', senha):
        break
    else:
        oculto = senha.replace(senha, '*'*len(senha))
        print(oculto)
        Word = False
        break

if Word:
    print('Senha Inválida!')