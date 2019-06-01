#005 - Biblioteca e Livro

class Livro():

    cod = None

    def __init__(self, t, a, cod = 0):
        self.__t = t
        self.__a = a
        self.cod = cod
        self.__totalAlugueis = 0

    def getTitulo(self):
        return self.__t
    
    def getAutor(self):
        return self.__a
    
    def getQtdAluguel(self):
        return self.__totalAlugueis

    def incQtdeAluguel(self):
        self.__totalAlugueis += 1

class Biblioteca():

    __alug = []
    __disp = []
    __proxCod = 1

    def addLivro(self, novo):
        novo.cod = self.__proxCod
        self.__disp.append(novo)
        self.__proxCod += 1
        return novo.cod
    
    def Alugar(self, cod):
        for k in range(len(self.__disp)):
            if self.__disp[k].cod == cod:
                disp = True
                indice = k
                break
        else:
            disp = False
        if disp:
            l = self.__disp.pop(indice)
            l.incQtdeAluguel()
            self.__alug.append(l)
        return disp
    
    def Devolver(self, cod):
        for k in range(len(self.__alug)):
            if self.__alug[k].cod == cod:
                dev = True
                indice = k
                break
        else:
            dev = False
        if dev:
            l = self.__alug.pop(indice)
            self.__disp.append(l)
        return dev
    
    def MaisAlugado(self):
        l = None
        qtdeAlug = 0
        for k in range(len(self.__alug)):
            n = self.__alug[k].getQtdAluguel()
            if n > qtdeAlug:
                l = self.__alug[k]
                qtdeAlug = n
        
        for k in range(len(self.__disp)):
            n = self.__disp[k].getQtdAluguel()
            if n > qtdeAlug:
                l = self.__disp[k]
                qtdeAlug = n
        
        texto = ''
        if l != None:
            texto = 'Livro Mais Alugado: %d vez(es)' %qtdeAlug
            texto += '\nTítulo: %s' %l.getTitulo()
            texto += '\nAutor: %s' %l.getAutor()
            texto += '\nCódigo: %d' %l.cod
        return texto

def imprimeMenu():
    print()
    print("----------------------------------------------")
    print("::   Bem vindo(a) à biblioteca do Dorgy     ::")
    print("::   Por favor, selecione a opcao desejada: ::")
    print("::   1. Cadastrar um livro                  ::")
    print("::   2. Alugar um livro                     ::")
    print("::   3. Devolver um livro                   ::")
    print("::   4. Exibir o livro mais alugado         ::")
    print("::   5. Sair do sistema                     ::")
    print("--------------------------------------------::")
    print(":::::: Digite a sua opcao: ")
    return input()
 
#programa principal:
bib = Biblioteca()
sair = False
 
while sair == False:
    op = imprimeMenu()
    if op == "5":
        sair = True
    elif op == "1": #inserir um livro
        t = str(input("Digite o titulo do livro: "))
        a = str(input("Digite os autores do livro: "))
        l = Livro(t, a)
        codigoInserido = bib.addLivro(l)
        print("Livro inserido - codigo: %d"%codigoInserido)
    elif op == "2": #alugar
        cod = int(input("Digite o codigo do livro que deseja ALUGAR: "))
        retorno = bib.Alugar(cod)
        if retorno: #conseguiu alugar
            print("Livro alugado com sucesso!")
        else:
            print("ERRO! O livro nao esta disponivel para aluguel")
 
    elif op == "3": #devolver
        cod = int(input("Digite o codigo do livro que deseja DEVOLVER: "))
        retorno = bib.Devolver(cod)
        if retorno: #conseguiu devolver
            print("Livro devolvido com sucesso!")
        else:
            print("ERRO! O livro nao estava alugado")
    elif op == "4": #livro mais alugado
        mensagem = bib.MaisAlugado()
        if mensagem != "":
            print(mensagem)
        else:
            print("Erro! Nao ha' nenhum livro alugado ainda!")
    else:
        print("Erro! Opcao invalida! Voce deve escolher uma opcao entre 1 e 5")