#177 - Jogo da Palavra Embaralhada

from random import shuffle

palavra = 'DORGIVAL'
emb = list(palavra)
shuffle(emb)
Embaralhado = ''.join(emb)
erros = 0

print(f'Palavra Embaralhada: {Embaralhado}')
while erros < 6:
    resposta = input('Decifre a Palavra: ').upper()
    if resposta == palavra and erros == 0:
        pCerta = resposta
        if pCerta == palavra:
            print('Excepcional! Você ganhou sem cometer erros!')
            print(f'Palavra Certa: {palavra}')
            break
    elif resposta == palavra and (1 <= erros < 6):
        pCerta = resposta
        if pCerta == palavra:
            print('Voce acertou!')
            print(f'Palavra certa: {palavra}')
            break
    else:
        erros += 1
        print(f'Você errou a {erros}° vez')
else:
    print(f'Infelizmente você perdeu o jogo. Resposta certa: {palavra}')

