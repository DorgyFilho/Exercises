#022 - Questão Extra 5: TV

class TV:

    def __init__(self, can = 1, vol = 0):
        self.can = can
        self.vol = vol
    
    def mostraStatus(self):
        return('Canal: %d\nVolume: %d' %(self.can, self.vol))
    
    def mudaCanal(self, novo):
        if 1 <= novo <= 100:
            self.can = novo
            return 'Canal alterado com sucesso!'
        else:
            return 'Canal indisponível!'
        
    def mudaVolume(self, novo):
        if 0 <= novo <= 25:
            self.vol = novo
            return 'Volume está dentro do nível aceitável.'
        else:
            return 'Volume inválido! Volume fora do nível aceitável.'

    # def __repr__(self):
    #     print('Canal: %d\nVolume: %d' %(self.can, self.vol))

def Menu():
    tv = TV()
    while True:
        print('Bem-vindo ao sistema Dorgy TV\n1-Mudar Canal\n2-Mudar Volume\n3-Status\n4-Sair')
        op = input('Digite a sua opção: ')
        if op == '1':
            can = input('Escolha o canal entre 1 e 100: ')          
            print(tv.mudaCanal(int(can)))
        elif op == '2':
            vol = input('Digite o volume entre 0 e 25: ')
            print(tv.mudaVolume(int(vol)))
        elif op == '3':
            print(tv.mostraStatus())
        elif op == '4':
            print('TV desligada com sucesso!')
            break

Menu()
            



