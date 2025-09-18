"""
Projeto: Sistema Bancário (Versão 2)

Com base na versão anterior do sistema bancário, adicione as seguintes funcionalidades complementares:

1. Limite de Transações Diárias
    - O sistema deve permitir no máximo 10 transações por dia (incluindo depósitos e saques).
    - Caso o usuário tente realizar uma transação após atingir o limite, o sistema deve exibir uma mensagem 
        informando que o número de transações diárias foi excedido.

2. Controle de Saques (regras mantidas da versão 1)
    - Continuam válidas as regras: máximo de 3 saques por dia e limite de R$ 500,00 por saque.

3. Registro de Data e Hora
    - Cada transação (depósito ou saque) deve ser registrada com a data e hora exata em que foi realizada.
    - Essas informações devem aparecer no extrato ao lado de cada movimentação.

4. Extrato Atualizado
    - O extrato deve exibir, em ordem, todas as transações do dia, mostrando:
        - Tipo da operação (Depósito ou Saque)
        - Valor da operação
        - Data e hora da operação
    - Ao final, deve exibir o saldo atual da conta.
"""


from datetime import date, time, datetime, timedelta, timezone

dia_atual = date.today()
limite_operacoes = 10
operacoes_diarias = 0


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

def realizar_deposito(carteira, depositos_extrato, operacoes_diarias):
    while True:
        
        if operacoes_diarias >= limite_operacoes:
            print('\nLimite de saques diários atingidos!')
            break
        
        try:
            valor_deposito = float(input('\nDigite o valor do depósito: '))
        except ValueError:
            print("\nIsso não é um número válido!")
            continue

        if valor_deposito < 0:
            print('\nNúmero inválido para depósito!')
            continue
        
        carteira += valor_deposito
        operacoes_diarias += 1
        depositos_extrato.append(valor_deposito)
        
        print(f'\nDeposito de R${valor_deposito:.2f} foi realizado com sucesso\n\nCarteira: R${carteira:.2f}')
        break
    return carteira, depositos_extrato, operacoes_diarias

def realizar_saque(carteira, saques_extrato, operacoes_diarias, limite_operacoes):
    while True:
        
        if operacoes_diarias >= limite_operacoes:
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
        operacoes_diarias += 1
        saques_extrato.append(valor_saque)
        
        print(f'\nSaque de R${valor_saque:.2f} foi realizado com sucesso\n\nCarteira: R${carteira:.2f}')
        break
    return carteira, saques_extrato, operacoes_diarias

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

def aumentar_dia(dia_atual):
    dia_atual += timedelta(days=1)
    
    return dia_atual