#193 - Cadastramento de Alunos

class Aluno():

    def __init__(self, nome=''):
        self.__Nome = nome
        self.__Notas = []
        self.__Cadastro = []
    
    def addAluno(self, novo):
        if novo not in self.__Cadastro:
            self.__Cadastro.append(novo)
        else:
            print('Aluno já cadastrado.')
    
    def addNota(self):
        notaAluno = []
        nome = input('Nome: ').upper()
        if nome in self.__Cadastro:
            for k in range(4): 
                nota = float(input('Nota: '))
                notaAluno.append(nota)
            self.__Notas.append(notaAluno)
    
        else:
            print('Aluno não consta em nosso cadastro.')
    
    def verBoletim(self, nome):
        if nome in self.__Cadastro:
            nomeIndex = self.__Cadastro.index(nome)
            print(self.__Notas[nomeIndex])

    def mostrarAlunos(self):
        print('Alunos cadastrados')
        for aluno in self.__Cadastro:
            print(aluno)

def Menu():
    Est = Aluno()
    print('Sistema de Cadastro')
    print()
    while True:
        print('Opções:\n1-Cadastrar Aluno\n2-Adicionar Notas\n3-Ver Boletim\n4-Listar Alunos Cadastrados\n5-Sair')
        op = input('Resposta: ')
        if op == '5':
            print('Programa Encerrado.')
            break
        else:
            if op == '1':
                nome = input('Nome: ').upper()
                Est.addAluno(nome)
            elif op == '2':
                Est.addNota()
            elif op == '3':
                busca = input('Aluno(a): ').upper()
                Est.verBoletim(busca)
            elif op == '4':
                Est.mostrarAlunos()

Menu()



