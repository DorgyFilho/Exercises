#004 - Programa de Teste: Questão 4

from Ex004 import *

nome = input('Nome: ')
curso = input('Curso: ')
TSD = int(input('Tempo Sem Dormir: '))
print()
Estudante = Aluno(nome, curso, TSD)
print('%d Horas' %Estudante.Estudar(12))
print()
print('%d Horas' %Estudante.Dormir(5))

