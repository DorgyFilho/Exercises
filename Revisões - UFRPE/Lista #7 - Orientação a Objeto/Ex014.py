#014 - Apartamento

class Apto():

    def __init__(self, num, placas = [], Ocupados = []):
        self.__num = num
        self.__placas = placas
        self.__Ocupados = Ocupados
    
    def getNum(self):
        return self.__num
    
    def getPlacas(self):
        return self.__placas
    
    def addPlaca(self, placa):
        resultado = 'Placa cadastrada com sucesso!'
        if len(self.__placas) < 3:
            if placa not in self.__placas:
                self.__placas.append(placa)
            else:
                resultado = 'Placa já consta no sistema.'
        else:
            resultado = 'Já existem três placas cadastradas.'
        return resultado
    
    def libEnt(self, placa):
        retorno = False
        if placa in self.__placas:
            if len(self.__Ocupados) < 2:
                self.__Ocupados.append(placa)
                retorno = True
            else:
                print('Estacionamento lotado.')
        else:
            print('Placa não consta no sistema.')
        return retorno
    
    def removePlaca(self, placa):
        if placa not in self.__Ocupados:
            self.__Ocupados.remove(placa)
        else:
            print('Vaga ocupada.')
    
    def libSaida(self, placa):
        self.__Ocupados.remove(placa)

class Garagem():

    def __init__(self):
        self.__Aptos = {}
        self.__Entrada = []
        self.__Saida = []
    
    def cadastrarAptos(self):
        Pessoa1 = Apto('101')
        Pessoa2 = Apto('102')
        Pessoa3 = Apto('103')
        Pessoa4 = Apto('104')
        self.__Aptos[Pessoa1.getNum()] = Pessoa1
        self.__Aptos[Pessoa2.getNum()] = Pessoa2
        self.__Aptos[Pessoa3.getNum()] = Pessoa3
        self.__Aptos[Pessoa4.getNum()] = Pessoa4
    
    def libEntrada(self, placa):
        entre = False
        for numero in self.__Aptos.values():
            if numero.libEnt(placa):
                entre = True
                break
        if entre:
            self.__Entrada.append(placa)
            print('Entrada autorizada!')
        else:
            print('Entrada não autorizada.')
    
    def addPlaca(self, placa, Apt):
        if Apt in self.__Aptos.keys():
            Ap = self.__Aptos[Apt]
            print(Ap.addPlaca(placa))
        else:
            print('Não cadastrado!')
    
    def remPlaca(self, placa, Apt):
        if Apt in self.__Aptos.keys():
            Ap = self.__Entrada[Apt]
            Ap.remPlaca(placa)

Cad = Garagem()
Cad.cadastrarAptos()
Cad.addPlaca('KKZ3186', '101')
Cad.addPlaca('DMZ1234', '101')
Cad.addPlaca('DMZ1234', '101')
Cad.libEntrada('KKZ3186')
Cad.libEntrada('KKZ3185')
