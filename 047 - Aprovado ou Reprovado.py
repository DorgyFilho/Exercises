#047 - Aprovado ou Reprovado

nota1Mat1 = float(input('Nota 1 da matéria 1: '))
nota2Mat1 = float(input('Nota 2 da matéria 1: '))
nota1Mat2 = float(input('Nota 1 da matéria 2: '))
nota2Mat2 = float(input('Nota 2 da matéria 2: '))
nota1Mat3 = float(input('Nota 1 da matéria 3: '))
nota2Mat3 = float(input('Nota 2 da matéria 3: '))

mat1 = (nota1Mat1+nota2Mat1)/2
mat2 = (nota1Mat2+nota2Mat2)/2
mat3 = (nota1Mat3+nota2Mat3)/2

if mat1 >= 7.0 and mat2 >= 7.0 and mat3 >= 7.0:
    print(f'Você foi aprovado! Você vai para o próximo nível.\nMatéria 1: {mat1:.2f}\nMatéria 2: {mat2:.2f}\nMatéria 3: {mat3:.2f}')
else:
    print('Infelizmente você não conseguiu ser aprovado. Tente mais uma vez.')
