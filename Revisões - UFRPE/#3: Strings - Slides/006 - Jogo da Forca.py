#006 - Jogo da Forca

palavra = 'DORGIVAL'
pCerta = ''
erros = 0

while erros < 6:
    letra = input('Digite a letra: ').upper()
    if letra in palavra:
        pCerta += letra

        sublinhados = 0
        for let in palavra:
            if let in pCerta:
                print(f'{let}', end=' ')
            else:
                print('_', end=' ')
                sublinhados += 1
        
        if sublinhados == 0 and erros == 0:
            print('Excepcional! Você teve 100% de acerto!')
            break
        elif sublinhados == 0 and (1 <= erros < 6):
            print('Você acertou!')
            break
    else:
        erros += 1
        print(f'Você errou a {erros}° tentativa')
else:
    print(f'Você perdeu o jogo. Resposta Certa: {palavra}')