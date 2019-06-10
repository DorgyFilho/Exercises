#193 - Cadastramento de Alunos

class Aluno():

    def __init__(self, nome=''):
        self.__Nome = nome
        # self.__Notas = []
        self.__Dados = {}
    
    def addAluno(self, novo):
        Boletim = []
        if novo not in self.__Dados:
            for k in range(1,5):
                nota = float(input('%d° Nota: ' %k))
                Boletim.append(nota)
            self.__Dados[novo] = Boletim
        else:
            print('Aluno já cadastrado.')
    
    # def addNota(self):
    #     notaAluno = []
    #     nome = input('Nome: ').upper()
    #     if nome in self.__Cadastro:
    #         for k in range(4): 
    #             nota = float(input('Nota %d: ' %k))
    #             notaAluno.append(nota)
    #         self.__Notas.append(notaAluno)
    
    #     else:
    #         print('Aluno não consta em nosso cadastro.')
    
    def verBoletim(self, nome):
        if nome in self.__Dados.keys():
            print(self.__Dados[nome])
        else:
            print('Aluno não encontrado.')
    
    def NomeNotas(self):
        # Lista = zip(self.__Cadastro, self.__Notas)
        # Infor = dict(Lista)
        for nome, boletim in self.__Dados.items():
            print('%s: %s' %(nome, boletim))


    def mostrarAlunos(self):
        print('Alunos cadastrados')
        for aluno in self.__Dados.keys():
            print(aluno)

def Menu():
    Est = Aluno()
    print('Sistema de Cadastro')
    print()
    while True:
        print('Opções:\n1-Cadastrar Aluno\n2-Ver Boletim\n3-Listar Alunos Cadastrados\n4-Listar Nomes e Notas\n0-Sair')
        op = input('Resposta: ')
        if op == '0':
            print('Programa Encerrado.')
            break
        else:
            if op == '1':
                nome = input('Nome: ').upper()
                Est.addAluno(nome)
            # elif op == '2':
            #     Est.addNota()
            elif op == '2':
                busca = input('Aluno(a): ').upper()
                Est.verBoletim(busca)
            elif op == '3':
                Est.mostrarAlunos()
            elif op == '4':
                Est.NomeNotas()

Menu()



