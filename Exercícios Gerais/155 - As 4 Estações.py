#155 - As 4 Estações

#1 - Inserção de Dados

repetir = 'S'
estacao = ''
while repetir == 'S':
    dia = int(input('Dia: '))
    if dia < 0 and dia > 31:
        print('Dia inválido!')
        continue
    else:
        mes = input('Mês: ').upper()

#2 - Condições - Mês

    if mes == 'JANEIRO' or mes == 'FEVEREIRO' or mes == 'MARÇO':
        estacao = 'Verão'
    elif mes == 'ABRIL' or mes == 'MAIO' or mes == 'JUNHO':
        estacao = 'Outono'
    elif mes == 'JULHO' or mes == 'AGOSTO' or mes == 'SETEMBRO':
        estacao = 'Inverno'
    elif mes == 'OUTUBRO' or mes == 'NOVEMBRO' or mes == 'DEZEMBRO':
        estacao = 'Primavera'
    else:
        print('Inválido!')

#3 - Condições - Mês + Dia
    
    if mes == 'MARÇO' and dia > 20:
        estacao = 'Outono'
    elif mes == 'JUNHO' and dia > 21:
        estacao = 'Inverno'
    elif mes == 'SETEMBRO' and dia > 22:
        estacao = 'Primavera'
    elif mes == 'DEZEMBRO' and dia > 21:
        estacao = 'Verão'

    print(f'A Estação Atual é {estacao}')

    print()
    print('Deseja Repetir a Operação? S/N')
    repetir = input('Resposta: ').upper()
    if repetir == 'N':
        print('Encerrado!')
        break

else:
    print('Opção Inválida!')
