#006 - Vale Eletrônico

class Vale():

    def __init__(self, idCard, nome, cpf):
        self.__idCard = idCard
        self.__nome = nome
        self.__cpf = cpf
        self.__saldo = 0

    def addSaldo(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            return 'Valor Inválido!'

    def VerificarSaldo(self):
        return ('O saldo é R$%.2f' %self.__saldo)

    def debito(self, valor):
        if valor >= 0:
            self.__saldo -= valor
        else:
            return 'Saldo Insuficiente.'

class VemEstudante(Vale):

    def __init__(self, idCard, nome, cpf, IE):
        Vale.__init__(self, idCard, nome, cpf)
        self.__IE = IE
    
    def pagar(self, valor):
        self.debito(valor/2)

class VemTrabalhador(Vale):
    def __init__(self, idCard, nome, cpf, empresa):
        Vale.__init__(self, idCard, nome, cpf)
        self.__empresa = empresa
    
    def debitar(self, valor):
        self.debito(valor)



