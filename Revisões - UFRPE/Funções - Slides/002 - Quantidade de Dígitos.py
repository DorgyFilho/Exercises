#002 - Quantidade de Dígitos

def QtdDigitos(num):
    resultado = len(num)
    return resultado

num = input('Digite um número: ')
if num.isdigit():
    Retorno = QtdDigitos(num)
    print(Retorno)
else:
    print('Inválido!')