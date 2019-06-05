#185 - Conta Corrente

class Conta:

    def __init__(self, nome, conta):
        self.nome = nome
        self.conta = conta
        self.saldo = 0
    
    def alterarNome(self, novo):
        self.nome = novo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            print('Valor inválido!')
    
    def retirar(self, valor):
        if valor > 0:
            self.saldo -= valor
        else:
            print('Valor inválido!')
    
    def InfoCliente(self):
        print('Nome: %s\nConta: %s\nSaldo: R$%.2f' %(self.nome, self.conta, self.saldo))

Cliente = Conta('Dorgival', '1234')
Cliente.InfoCliente()
print()
Cliente.depositar(1000)
Cliente.InfoCliente()
Cliente.retirar(500)
Cliente.InfoCliente() 

