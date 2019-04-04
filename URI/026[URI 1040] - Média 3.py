#026 - Média 3

linha = input('').split(' ')
a = float(linha[0])
b = float(linha[1])
c = float(linha[2])
d = float(linha[3])
pA = 2
pB = 3
pC = 4
pD = 1

media = ((a*pA) + (b*pB) + (c*pC) + (d*pD))/10

if media >= 7.0:
    print('Media: %.1f' %media)
    print('Aluno aprovado.')

elif 5.0 <= media < 7.0:
    print('Media: %.1f' %media)
    print('Aluno em exame.')
    nExame = float(input())
    print('Nota do exame: %.1f' %nExame)
    novaMedia = (media + nExame)/2
    if novaMedia >= 5.0:
        print('Aluno aprovado.')
        print('Media final: %.1f' %novaMedia)
    else:
        print('Aluno reprovado.')
        print('Media Final: %.1f' %novaMedia)

else:
    print('Media: %.1f' %media)
    print('Aluno reprovado.')