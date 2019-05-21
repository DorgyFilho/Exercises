#010 - Fazenda

while True:
    print('1-Cadastrar Temperaturas\n2-Exibir Temperaturas\n3-Sair')
    print()
    op = input('Digite a sua escolha: ')
    if op == '1':
        data = input('Data: ')
        hora = input('Hora: ')
        temp = input('Temp: ')
        arq = open(input('Arquivo: '), 'a', encoding='utf-8')
        arq.write(f'{data} {hora} {temp}  ')
        arq.close()
    elif op == '2':
        arq = open(input('Arquivo: '), encoding='utf-8')
        print('Data   Hora   Temperatura')
        conteudo = arq.read()
        print(conteudo)
        arq.close()
    elif op == '3':
        print('Encerrado!')
        break