#001 - Televisor

class TV():

    def __init__(self, can, vol):
        self.canal = can
        self.volume = vol
    
    def mudaCanal(self, C):
        if C.isdigit():
            if 1 <= int(C) <= 100:
                self.canal = C
                return self.canal
            else:
                return 'Canal não disponível'
        else:
            return 'Apenas números podem ser digitados'

    def mudaVolume(self, V):
        if V.isdigit():
            if 0 <= int(V) <= 50:
                self.volume = V
                return self.volume
            else:
                return 'Volume fora do limite do aceitável'
        else:
            return 'Apenas números podem ser digitados'
    def __repr__(self):
        return ('Canal: %d\nVolume: %d' %(int(self.canal), int(self.volume)))

def Menu():
    while True:
        print('Menu:\n1-Ligar\n2-Mudar Canal e Volume\n3-Sair')
        print()
        op = input('Resposta: ')
        if op == '1':
            can = input('Escolha o canal: ') 
            vol = input('Escolha o volume: ')
            Tv = TV(can, vol)
            print(Tv)
            print()
        elif op == '2':
            Can = input('Escolha o canal: ')
            Vol = input('Escolha o volume: ')
            Troca = TV(Can, Vol)
            print(Troca.mudaCanal(Can))
            print(Troca.mudaVolume(Vol))
            print(Troca)
            print()
        elif op == '3':
            print('Sistema Desligado')
            break

Menu()