#158 -  Validação de Senha
#Critérios de Validação
#Pelo menos 1 letra entre a-z e 1 letra entre A-Z
#Pelo menos 1 número entre 1 e 9
#Pelo menos 1 caractere especial [$#@]
#Mínimo: 4
#Máximo: 12
import re

senha = input('Digite a sua senha: ')
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
        print('Senha Válida')
        Word = False
        break

if Word:
    print('Senha Inválida!')
    