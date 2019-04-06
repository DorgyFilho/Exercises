#098 - Menor e Posição

#1 - Intro
N = int(input('')) #Quantidade de entradas
numeros = []
k = list(map(int, input().split())) #Digitar os valores

#2 - Desenvolvimento
for i in range(N):
    numeros.insert(i, k[i])
    menor = min(numeros) #Obter o menor número.
print('Menor valor: %d' %menor)

#3 - Conclusão
for i in range(N):
    if numeros[i] == menor: #Te achei!
        pos = i #Posição do menor número
print('Posicao: %d' %pos)