#003 - Livro

class Livro():

    def __init__(self, titulo, autor, pag, preco):
        self.titulo = titulo
        self.autor = autor
        self.pag = pag
        self.preco = preco
    
    def setPreco(self, novoPreco):
        self.preco = novoPreco
    
    def getPreco(self):
        return self.preco
    
    def armazenar(self):
        self.Data = {'Título': self.titulo, 'Autor': self.autor, 'Qtde Pág': self.pag, 'Preço': self.preco}
        return self.Data
        
# titulo = input('Titulo do Livro: ')
# autor = input('Autor do Livro: ')
# pag = input('Quantidade de Páginas: ')
# preco = float(input('Preço: '))
# Book = Livro(titulo, autor, pag, preco)
# print(Book.armazenar())
# print(Book.setPreco(50))
# print()
# print(Book.armazenar())

