#120 - Número de Veículos Em Uma Cidade

maiorIndice = 0
menorIndice = 1000000
somaGeral = 0
mediaGeral = 0
somaCidadesMais2000 = 0
mediaCidadesMais2000 = 0
somaCidadesMenos2000 = 0
mediaCidadesMenos2000 = 0
cidMenosDe2000 = 0
cidMaisDe2000 = 0
codMaiorIndice = 0
codMenorIndice = 0

for i in range(1,6):
    cod = int(input(f'Codigo da {i}° Cidade: '))
    nVeiculos = int(input(f'Número de Veículos na {i}° Cidade: '))
    nAcid = int(input(f'Número de acidentes na {i}° Cidade: '))
    somaGeral += nVeiculos
    mediaGeral = somaGeral/i
    if nVeiculos < 2000:
        cidMenosDe2000 += 1
        somaCidadesMenos2000 += nVeiculos
        mediaCidadesMenos2000 = somaCidadesMenos2000/cidMenosDe2000
    if nVeiculos >= 2000:
        cidMaisDe2000 += 1
        somaCidadesMais2000 += nVeiculos
        mediaCidadesMais2000 = somaCidadesMais2000/cidMaisDe2000
    if nAcid > maiorIndice:
        maiorIndice = nAcid
        codMaiorIndice = cod
    if nAcid < menorIndice:
        menorIndice = nAcid
        codMenorIndice = cod

print(f'Soma Geral De Veículos Em 1999: {somaGeral}')
print(f'Media Geral De Veículos Em 1999: {mediaGeral:.0f}')
print(f'Soma de Veículos Em Cidades Com Menos de 2000 Veículos: {somaCidadesMenos2000}')
print(f'Média de Veículos Em Cidades Com Menos de 2000 Veículos: {mediaCidadesMenos2000:.2f}')
print(f'Soma de Veículos Em Cidades Com Mais de 2000 Veículos: {somaCidadesMais2000}')
print(f'Média de Veículos Em Cidades Com Mais de 2000 Veículos: {mediaCidadesMais2000:.2f}')
print(f'Maior Número de Acidentes Registrados: {maiorIndice}')
print(f'Menor Número de Acidentes Registrados: {menorIndice}')
print(f'Cidade Com Maior Índice de Acidentes: {codMaiorIndice}')
print(f'Cidade Com Menor Índice de Acidentes: {codMenorIndice}')

