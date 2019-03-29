#009 - Altura e Sexo

maiorAltura = 0
menorAltura = 1000
somaAlturaMulheres = 0
qtdHomens = 0
qtdMulheres = 0
sexoMaisAlta = ''
for i in range(1,16):
    altura = float(input('Altura: '))
    sexo = input('Sexo - M/F: ').upper()
    if sexo != 'M' and sexo != 'F':
        print('Sexo inválido!')
        exit()
    else:
        if altura > maiorAltura:
            maiorAltura = altura
            sexoMaisAlta = sexo

        if altura < menorAltura:
            menorAltura = altura

        if sexo == 'M':
            qtdHomens += 1

        else:
            qtdMulheres += 1
            somaAlturaMulheres += altura

mediaAlturaMulheres = somaAlturaMulheres/qtdMulheres

print(f'Qtd. Mulheres: {qtdMulheres}')
print(f'Qtd. Homens: {qtdHomens}')
print(f'Sexo da Pessoa Mais Alta: {sexoMaisAlta}')
print(f'Pessoa Com a Maior Altura: {maiorAltura}')
print(f'Soma da Altura das Mulheres: {somaAlturaMulheres}')
print(f'Média da Altura das Mulheres: {mediaAlturaMulheres:.2f}')
