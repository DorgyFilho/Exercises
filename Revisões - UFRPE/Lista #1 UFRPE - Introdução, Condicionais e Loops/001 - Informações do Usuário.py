#001 - Informações do Usuário

nome = input('Nome: ')
endereco = input('Digite o seu endereço: ')
curso = input('Curso de Graduação: ')
idade = int(input('Idade: '))
altura = float(input('Altura: '))
peso = float(input('Peso: '))

print(f'{nome}, residente no endereço {endereco}, é aluno do curso de {curso}. Ele(a) tem {idade} anos, {altura} m de altura e {peso} kg.')
