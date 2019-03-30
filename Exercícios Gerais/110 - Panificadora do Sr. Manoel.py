#110 - Panificadora do Sr. Manoel

repetir = 'S'
while repetir == 'S':
    pUnitPao = float(input('Informe o preço unitário do pão - Ex: 0.20: '))
    qtdPao = int(input('Quantidade de Pães a ser adquirida: '))
    if qtdPao < 1 or qtdPao > 50:
        print('Só podem ser adquiridos até 50 paẽs. Tente novamente.')
        continue
    else:
        for i in range(1, qtdPao+1):
            total = i*pUnitPao
            print(f'{i} --- Valor: R${total:.2f}')
    print()
    print('Deseja repetir a operação? S ou N')
    repetir = input('Resposta: ').upper()
    if repetir == 'N':
        print('Programa Encerrado.')
        break
else:
    print('Opção Inválida!')
