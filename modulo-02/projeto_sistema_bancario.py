'''
Projeto: Sistema Bancário (Versão 1)

- O sistema deve permitir a gestão de uma única conta bancária, possibilitando as seguintes operações:

1. Depósito

    - Deve ser possível depositar valores positivos na conta.
    - Todos os depósitos realizados devem ser armazenados em uma variável para consulta futura no extrato.

2. Saque

    - O usuário pode realizar até 3 saques diários, com limite máximo de R$ 500,00 por saque.
    - Caso o usuário não tenha saldo suficiente, o sistema deve exibir uma mensagem informando que o saque não pode ser realizado por falta de saldo.
    - Todos os saques realizados devem ser armazenados em uma variável para consulta futura no extrato.

3. Extrato

    - Deve listar todos os depósitos e saques realizados na conta.
    - Ao final, deve exibir o saldo atual da conta.
    - Os valores devem ser exibidos no formato R$ xxx.xx, exemplo: 1500.45 = R$ 1500.45.
'''

def mostrar_menu():
    while True:
        print("\n============ SISTEMA BANCÁRIO ============")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Ver Extrato")
        print("0 - Sair\n")
        
        try:
            option = int(input('Escolha uma das opções acima: '))
        except ValueError:
            print("Isso não é um número válido!")
            continue
        
        if option < 0 or option > 3:
            print('Número inválido')
            continue
        
        return option

def realizar_deposito():
    while True:
        try:
            valor_deposito = float(input('Digite o valor do depósito: '))
        except ValueError:
            print("Isso não é um número válido!")
            continue

        if valor_deposito < 0:
            print('Número inválido para depósito!')
            continue
        
        carteira += valor_deposito
        depositos_esxtrato.append(valor_deposito)
        
        return print(f'Deposito de R${valor_deposito:.2f} foi realizado com sucesso \n Carteira: R${carteira}')

carteira = 0
depositos_esxtrato = []
limite_saques = 3
saques_extrato = []


