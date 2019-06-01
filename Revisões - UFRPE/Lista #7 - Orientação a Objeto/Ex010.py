#010 - Locadora

class Filme():

    def __init__(self, N, G, D = True):
        self.__nome = N
        self.__genero = G
        self.__disp = D
    
    def setDisp(self, Disp):
        self.__disp = Disp
    
    def setNome(self, nome):
        self.__nome = nome
    
    def setGen(self, gen):
        self.__genero = gen
    
    def getDisp(self):
        return self.__disp
    
    def getNome(self):
        return self.__nome
    
    def getGen(self):
        return self.__genero
    
    def Catalogo(self):
        print('Nome: %s, Gênero: %s, Disponível: %s' %(self.__nome, self.__genero, self.__disp))

class Locadora():

    def __init__(self):
        self.__Catalogo = []
        self.filmesMaisProcurados()
    
    def filmesMaisProcurados(self):
        Filme1 = Filme('Um Amor Para Recordar', 'Romance')
        self.__Catalogo.append(Filme1)
        Filme2 = Filme('Caçada Mortal', 'Ação')
        self.__Catalogo.append(Filme2)
        Filme3 = Filme('Final Fantasy', 'Ação')
        self.__Catalogo.append(Filme3)
    
    def OrgPorGen(self):
        Acao = []
        Drama = []
        Romance = []

        for k in self.__Catalogo:
            gen = k.getGen()
            if gen == 'Ação':
                Acao.append(k)
            elif gen == 'Drama':
                Drama.append(k)
            elif gen == 'Romance':
                Romance.append(k)

        print('Ação:')
        for filme in Acao:
            filme.Catalogo()
        
        print('Drama:')
        for filme in Drama:
            filme.Catalogo()
        
        print('Romance:')
        for filme in Romance:
            filme.Catalogo()
        
    def Alugar(self, nome):
        for k in self.__Catalogo:
            if k.getNome() == nome:
                if k.getDisp():
                    k.setDisp(False)
                    print('Filme Alugado!')
                else:
                    print('Não disponível')
                break
                
            
Locar = Locadora()
Locar.Alugar('Final Fantasy')
Locar.Alugar('Caçada Mortal')
