#005 - Facebook

class contaFacebook():

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.amigos = []
    
    def addAmigo(self, novo):
        self.amigos.append(novo)
    
    def conhecePessoa(self, friend):
        if friend in self.amigos:
            return 'Sim'
        else:
            return 'Não'
    
    def listarAmigo(self):
        Amigo = ''
        for a in self.amigos:
            Amigo = a + ', '
        return Amigo[:-2]

nome = input('Nome: ').lower()
idade = input('Idade: ')
Novo = contaFacebook(nome, idade)
Add = input('Adicione um(a) amigo(a): ')
Novo.addAmigo(Add)
Friend = input('Digite o nome de um amigo: ')
print(Novo.conhecePessoa(Friend))
print(Novo.listarAmigo())


