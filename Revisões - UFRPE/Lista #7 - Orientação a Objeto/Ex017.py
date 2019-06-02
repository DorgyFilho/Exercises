#017 - Loja

class Func:

    def __init__(self, nome, cargo, salario, cpf):
        self.__nome = nome
        self.__cargo = cargo
        self.__salario = salario
        self.__cpf = cpf
    
    def pegaSalario(self):
        return self.__salario

class Vendedor(Func):

    def __init__(self, nome, cargo, salario, cpf, venda, metaMes):
        Func.__init__(self, nome, cargo, salario, cpf)
        self.__metaMes = metaMes
        self.__vendas = venda

    def setMetaMes(self, meta):
        self.__metaMes = meta
    
    def alcancouMetas(self):
        return self.__vendas >= self.__metaMes
    
    def getVendas(self):
        return self.__vendas
    
class Loja():

    def __init__(self, cod, meta, ger, ven = []):
        self.__cod = cod
        self.__meta = meta
        self.__ger = ger
        self.__ven = ven
   
    def getCod(self):
        return self.__cod
    
    def getMeta(self):
        return self.__meta

    def addVendedor(self, novo):
        self.__ven.append(novo)
    
    def obterTotalVendas(self):
        total = 0.0
        for fun in self.__ven:
            total += fun.getVendas()
        return total
    
    def funcMetasCumpridas(self):
        funcionarios = [fun for fun in self.__ven if fun.alcancouMeta()]
        return funcionarios

    def funcMetasNaoCumpridas(self):
        funcionarios = [fun for fun in self.__ven if not fun.alcancouMeta()]
        return funcionarios

    def custoLoja(self):

        CustoTotal = 0

        for func in self.__ven:
            CustoTotal += func.pegaSalario()
            if func.alcancouMetas():
                CustoTotal += func.pegaSalario() * 0.1
        CustoTotal += self.__ger.pegaSalario()
        if self.obterTotalVendas() > self.__meta:
            CustoTotal += self.__ger.pegaSalario()*0.2
        return CustoTotal

class Sistema():

    def __init__(self, Lojas = []):
        self.__Rede = Lojas
    
    
    def lojaMaiorLucro(self):
        MaiorLucro = ''
        maior = 0
        for loja in self.__Rede:
            lucro = loja.obterTotalVendas() - loja.custoLoja()
            if lucro > maior:
                maior = lucro
                MaiorLucro = loja
        return MaiorLucro
    
    def getLoja(self, cod):
        procurada = ''
        for estabelecimento in self.__Rede:
            if estabelecimento.getCod() == cod:
                procurada = estabelecimento
                break
        return procurada
    

    def addLoja(self, novaLoja):
        self.__Rede.append(novaLoja)
    
    
    def cumpriuMeta(self):
        cumpMeta = [loja for loja in self.__Rede if loja.obterTotalVendas >= loja.getMeta()]
        return cumpMeta

class Gerencial():

    def cadastrarFunc(self):
        nome = input('Seu nome: ')
        funcao = input('Seu cargo: ')
        salario = float(input('Salário: '))
        cpf = input('CPF: ')
        if nome != '':
            Pessoa = Func(nome, funcao, salario, cpf)
        return Pessoa

    
# Cadastros = Gerencial()
# Dorgival = Cadastros.cadastrarFunc()
# Cecilia = Vendedor('Cecilia', 'Vendedora', 3000, '4321', 12000, 15000)
# L1 = Loja(123, 30000, Dorgival)
# L1.addVendedor(Cecilia)
# print('Total de Vendas: %.2f' %L1.obterTotalVendas())

    


