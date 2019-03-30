#083 - Usuário e Senha

while True:
    login = input('Login: ')
    senha = input('Senha: ')
    if login == senha:
        print('Cadastro inválido. Tente novamente.')
        continue
    else:
        print(f'Login: {login}\nSenha: {senha}' )
        break
