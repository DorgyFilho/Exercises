#001 - CPF

def cpf(num):
    if num[0:3].isdigit() and num[4:7].isdigit() and num[8:11].isdigit() and num[12:].isdigit() and '.' in num[3] and '.' in num[7] and '-' in num[11]:
        return f'{num} é um CPF válido!'
    else:
        return f'{num} é um CPF inválido!'

num = input('CPF: ')
resultado = cpf(num)
print(resultado)