#001 - Ingresso

class Ingresso:

    atual = None

    def __init__(self, atual):
        self.atual = atual
    
    def imprimirPreco(self):
        return('Preço atual do ingresso: R$%.2f' %self.atual)

class VIP(Ingresso):

    vip = None
    
    def __init__(self, vip):
        Ingresso.__init__(self, vip)
        self.vip = vip
    
    def imprimirPrecoVip(self):
        return('O valor do ingresso VIP é R$%.2f' %self.vip)
    
atual = float(input('Valor atual do ingresso: '))
add = float(input('Valor adicional para obter o ingresso VIP: '))
novoValor = atual + add
Normal = Ingresso(atual)
print(Normal.imprimirPreco())
Especial = VIP(novoValor)
print(Especial.imprimirPrecoVip())
