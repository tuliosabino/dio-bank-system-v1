menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=> '''

saldo = 0
limite = 500
extrato = ''
num_saques = 0
espacador = 50
LIMITE_SAQUES = 3
SEP = ' | '


while True:
    print(' Menu '.center(espacador, '#'))
    opcao = input(menu)

    if opcao == 'd':
        print(' Depósito '.center(espacador, '#'), '\n\n')
        deposito = float()
        while True:
            deposito = float(input('Digite o valor que deseja depositar: '))
            if deposito > 0:
                saldo += deposito
                extrato += f'Depósito: || R$ {deposito:.2f}' + SEP
                print('\nDepósito realizado com sucesso.\n\n'
                      f'Saldo atual: R$ {saldo:.2f}.\n\n')
                break
            else:
                print('O valor não é válido, digite um número maior que 0!\n')

    elif opcao == 's':
        print(' Saque '.center(espacador, '#'), '\n\n')

        while True:

            if saldo == 0:
                print('Você não tem nenhum saldo.\n\n')
                break

            valor_saque = float()
            if num_saques < LIMITE_SAQUES:
                valor_saque = float(input('Digite o valor que deseja sacar: '))

            elif num_saques >= LIMITE_SAQUES:
                print('Você atingiu o limite de saques diários '
                      f'atual que é de {LIMITE_SAQUES} saques.\n\n')
                break

            if valor_saque > 500:
                print('Valor do saque maior que o permitido, '
                      f'insira um valor menor que {limite}.\n')

            elif valor_saque <= 0:
                print('Valor inválido, digite um número maior que 0!\n')

            elif valor_saque > saldo:
                print('\nO valor do saque é maior que o saldo atual, '
                      f'insira um valor menor ou igual a R$ {saldo:.2f}\n')

            elif valor_saque > 0 and valor_saque <= saldo:
                saldo -= valor_saque
                num_saques += 1
                extrato += f'Saque: || R$ {valor_saque:.2f}' + SEP
                print('\n\nSaque realizado com sucesso.\n'
                      f'Saldo atual é de R$ {saldo:.2f}\n\n')
                break

    elif opcao == 'e':
        print(' Extrato '.center(espacador, '#'), '\n\n')

        if extrato:
            lista_saques = extrato.rstrip(SEP).split(SEP)

            print('\nAqui estão todas as suas operações:\n')

            for operacao in lista_saques:
                tipo, valor = operacao.split('||')
                print(tipo.center(15), valor)

            print(f'\nSaldo atual: R$ {saldo:.2f}\n\n')

        else:
            print('Não foram realizadas movimentações.\n\n')

    elif opcao == 'q':
        print('Sair...')
        break

    else:
        print('Operação inválidam por favor selecione '
              'novamente a operação desejada.')
