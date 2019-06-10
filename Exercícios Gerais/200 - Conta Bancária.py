#200 - Conta Bancária V2

class Conta:

    def __init__(self, nome, conta, saldo = 0):
        self.nome = nome
        self.conta = conta
        self.saldo = saldo
    
    def pegaNome(self):
        return self.nome
    
    def credito(self, valor):
        if valor > 0:
            self.saldo += valor
            print('Valor creditado com sucesso.')
        else:
            print('Não foi possível realizar a operação.')
    
    def debito(self, valor):
        if valor > 0:
            self.saldo -= valor
            print('Valor debitado com sucesso.')
        else:
            print('Não foi possível realizar a operação.')
    
    def infoCliente(self):
        return 'Nome: %s\nConta: %s\nSaldo: R$%.2f' %(self.nome, self.conta, self.saldo)

Dorgival = Conta('Dorgival', '1234', 1000)
print(Dorgival.infoCliente())
print()
Dorgival.credito(1000)
print(Dorgival.infoCliente())
print()
Dorgival.debito(800)
print(Dorgival.infoCliente())