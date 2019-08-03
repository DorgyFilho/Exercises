#156 - Papagaio Poliglota

def jogo():
    while True:
        try:
            acao = input()
            if acao == 'esquerda':
                print('ingles')
            elif acao == 'direita':
                print('frances')
            elif acao == 'nenhuma':
                print('portugues')
            elif acao == 'as duas':
                print('caiu')
        except EOFError:
            break

jogo()

