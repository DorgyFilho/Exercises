#008 - Acima de 30

agenda = {}
while True:
    cpf = input('CPF: ')
    if cpf.lower() == 'fim':
        break
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    agenda[cpf] = {'Nome': nome, 'Idade': idade}

acimade30 = []
pessoas30 = []
abaixode30 = []
ac30 = {}
ab30 = {}
p30 = {}

for key in agenda:
    if agenda[key]['Idade'] > 30:
        acimade30.append(key)
    elif agenda[key]['Idade'] < 30:
        abaixode30.append(key)
    else:
        pessoas30.append(key)

print('Acima de 30:')
for i in acimade30:
    ac30[i] = agenda.pop(i)
    print(ac30)

print()
print('Abaixo de 30:')
for j in abaixode30:
    ab30[j] = agenda.pop(j)
    print(ab30)

print()
print('Pessoas com 30 anos:')
for k in pessoas30:
    p30[k] = agenda.pop(k)
    print(p30)