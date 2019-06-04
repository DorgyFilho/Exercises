#003 - Teste da Questão 003

from Ex003 import *

titulo = input('Titulo do Livro: ')
autor = input('Autor do Livro: ')
pag = input('Quantidade de Páginas: ')
preco = float(input('Preço: '))
Book = Livro(titulo, autor, pag, preco)
biblioteca = []
biblioteca.append(Book)

for l in biblioteca:
    l.imprimirInfo()
# print(Book.armazenar())
# Book.setPreco(50)
# print()
# print(Book.armazenar())


