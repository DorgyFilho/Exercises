#009 - Mês de Nascimento

def mes(data):
    listaMes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
    'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    if data == '' or data[3:5] == '' or data[6:] == '' or data.isalpha() or data[3:5].isalpha() or data[6:].isalpha():
        return 'NULL'
    else:
        novaData = data.split('/')
        mes = int(novaData[1])
        if type(mes) == int:
            if 1 <= mes <= 12:
                return f'Você nasceu no dia {data[0:2]} de {listaMes[mes-1]} de {data[6:]}'
        else:
            return 'Inválido!'