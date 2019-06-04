#004 - Programa de Teste: Questão 4

from Ex004 import *

nome = input('Nome: ')
curso = input('Curso: ')
print()
Estudante = Aluno(nome, curso)
Estudante.Estudar(7)
Estudante.Dormir(5)
Estudante.Estudar(7)
Estudante.SemDormir()

