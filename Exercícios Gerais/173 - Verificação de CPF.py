#173 - Verificação de CPF

cpf = input('Digite o seu CPF no formato XXX.XXX.XXX-XX: ')
tamCPF = len(cpf)
if '.' in cpf[3] and '.' in cpf[7] and '-' in cpf[11] and tamCPF == 14:
    print('CPF Válido!')
else:
    print('CPF inválido!')