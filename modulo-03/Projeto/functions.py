

def mostrar_menu():
    while True:
        print("\n============ SISTEMA BANCÁRIO ============")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Ver Extrato")
        print("0 - Sair")
        
        try:
            option = int(input('\nEscolha uma das opções acima: '))
        except ValueError:
            print("\nIsso não é um número válido!")
            continue
        
        if option < 0 or option > 3:
            print('\nNúmero inválido')
            continue
        
        return option

def realizar_deposito(carteira, depositos_extrato):
    while True:
        try:
            valor_deposito = float(input('\nDigite o valor do depósito: '))
        except ValueError:
            print("\nIsso não é um número válido!")
            continue

        if valor_deposito < 0:
            print('\nNúmero inválido para depósito!')
            continue
        
        carteira += valor_deposito
        depositos_extrato.append(valor_deposito)
        
        print(f'\nDeposito de R${valor_deposito:.2f} foi realizado com sucesso\n\nCarteira: R${carteira:.2f}')
        break
    return carteira, depositos_extrato

def realizar_saque(carteira, saques_extrato, saque_diario, limite_saques):
    while True:
        
        if saque_diario >= limite_saques:
            print('\nLimite de saques diários atingidos!')
            break
        
        try:
            valor_saque = float(input('\nDigite o valor do saque (Limite max.: R$500,00): '))
        except ValueError:
            print("\nIsso não é um número válido!")
            continue
        
        if valor_saque < 0:
            print('\nValor inválido!')
            continue
        elif valor_saque > 500:
            print('\nLimite máximo por saque: R$500,00')
            continue
        elif valor_saque > carteira:
            print(f'\nSaldo insuficiente! - Carteira: R${carteira}')
            break
        
        carteira -= valor_saque
        saque_diario += 1
        saques_extrato.append(valor_saque)
        
        print(f'\nSaque de R${valor_saque:.2f} foi realizado com sucesso\n\nCarteira: R${carteira:.2f}')
        break
    return carteira, saques_extrato, saque_diario

def consultar_extrato(depositos_extrato, saques_extrato, carteira):
    print('\n=============== EXTRATO ===============')
    
    for i, deposito in enumerate(depositos_extrato):
        print(f'Deposito {i+1}: R${deposito:.2f}')

    print()
    for i, saque in enumerate(saques_extrato):
        print(f'Saque {i+1}: R${saque:.2f}')
    
    print(f'\nTotal de depósitos: R${sum(depositos_extrato):.2f}')
    print(f'Total de saques: R${sum(saques_extrato):.2f}')

    print(f'\nSaldo atual: R${carteira:.2f}')
