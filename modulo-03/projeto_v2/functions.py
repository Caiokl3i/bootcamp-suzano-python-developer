"""
Projeto: Sistema Bancário (Versão 2)

Com base na versão anterior do sistema bancário, adicione as seguintes funcionalidades complementares:

1. Modularização
    - Criar funções separadas para cada operação existente:
        - Sacar
        - Depositar
        - Visualizar extrato/histórico

2. Criar Usuário (Cliente do Banco)
    - O programa deve armazenar os usuários em uma lista.
    - Um usuário deve conter os seguintes dados:
        - Nome
        - Data de nascimento
        - CPF (somente números)
        - Endereço (formato: logradouro, nro - bairro - cidade/sigla estado)
    - Restrições:
        - Não pode haver dois usuários com o mesmo CPF.

3. Criar Conta Corrente
    - O programa deve armazenar as contas em uma lista.
    - Uma conta deve conter:
        - Agência (fixo: "0001")
        - Número da conta (sequencial, iniciando em 1)
        - Usuário (cliente) vinculado
    - Regras:
        - O usuário pode ter mais de uma conta.
        - Uma conta pertence a somente um usuário.

Resumo das Funcionalidades:
    - Depositar
    - Sacar
    - Visualizar Extrato
    - Criar Usuário
    - Criar Conta Corrente
"""

from datetime import date, time, datetime, timedelta, timezone

def mostrar_menu(dia_atual, limite_operacoes, limite_diario):
    while True:
        print("\n============ SISTEMA BANCÁRIO ============")
        print(f'Dia de hoje - {dia_atual.strftime("%d/%m/%Y")}')
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Ver Extrato")
        print("4 - Dormir (aumentar dia)")
        print("0 - Sair")
        print(f'\nOperações diárias (Max. {limite_operacoes}): {limite_diario}')
        
        try:
            option = int(input('\nEscolha uma das opções acima: '))
        except ValueError:
            print("\nIsso não é um número válido!")
            continue
        
        if option < 0 or option > 4:
            print('\nNúmero inválido')
            continue
        
        return option

def realizar_deposito(carteira, depositos, operacoes_diarias, limite_operacoes, dia_atual):
    while True:
        
        if operacoes_diarias >= limite_operacoes:
            print('\nO número de transações diárias foi excedido!')
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
        
        depositos.append({'data_deposito': dia_atual, 'valor': valor_deposito})
        
        print(f'\nDeposito de R${valor_deposito:.2f} foi realizado com sucesso\n\nCarteira: R${carteira:.2f}')
        break
    return carteira, depositos, operacoes_diarias

def realizar_saque(carteira, saques, operacoes_diarias, limite_operacoes, dia_atual):
    while True:
        
        if operacoes_diarias >= limite_operacoes:
            print('\nO número de transações diárias foi excedido!')
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
        
        saques.append({'data_saque': dia_atual, 'valor': valor_saque})
        
        print(f'\nSaque de R${valor_saque:.2f} foi realizado com sucesso\n\nCarteira: R${carteira:.2f}')
        break
    return carteira, saques, operacoes_diarias

def consultar_extrato(depositos, saques, carteira):
    total_saques = 0
    total_depositos = 0
    
    print('\n=============== EXTRATO ===============\n')
    print('Depositos:')
    for deposito in depositos:
        print(f'. R${deposito['valor']:.2f} - {deposito['data_deposito'].strftime("%d/%m/%Y")} / {deposito['data_deposito'].hour}:{deposito['data_deposito'].minute}')
        total_depositos += deposito['valor']
    
    print()
    print('Saques:')
    for saque in saques:
        print(f'. R${saque['valor']:.2f} - {saque['data_saque'].strftime("%d/%m/%Y")} / {saque['data_saque'].hour}:{saque['data_saque'].minute}')
        total_saques += saque['valor']
    
    print(f'\nTotal de depósitos: R${total_depositos:.2f}')
    print(f'Total de saques: R${total_saques:.2f}')

    print(f'\nSaldo atual: R${carteira:.2f}')

def aumentar_dia(dia_atual, operacoes_diarias):
    dia_atual += timedelta(days=1)
    operacoes_diarias = 0
    
    return dia_atual, operacoes_diarias

# Pronto