#182 - TV

class TV:

    def __init__(self, C = 1, V = 0):
        self.can = C
        self.vol = V
    
    def statusTV(self):
        return 'Canal: %d\nVolume: %d' %(int(self.can), int(self.vol))
    
    def mudaCan(self, novo):
        if novo.isdigit():
            if 1 <= int(novo) <= 200:
                self.can = novo
                print('Canal alterado com sucesso!')
            else:
                print('Canal inválido')
        else:
            print('Informação Inválida!')
    
    def mudaVol(self, novo):
        if novo.isdigit():
            if 0 <= int(novo) <= 25:
                self.vol = novo
                print('Volume está dentro do nível tolerável.')
            else:
                print('Volume está fora do nível tolerável.')
        else:
            print('Informação Inválida!')
    
def Menu():
    tv = TV()
    while True:
        print('Dorgy TV\n1-Alterar Canal\n2-Alterar Volume\n3-Status\n4-Sair')
        print()
        op = input('Digite sua opção: ')
        if op == '1':
            can = input('Canal: ')
            tv.mudaCan(can)
        elif op == '2':
            vol = input('Volume: ')
            tv.mudaVol(vol)
        elif op == '3':
            print(tv.statusTV())
        elif op == '4':
            print('TV desligada.')
            break

Menu()