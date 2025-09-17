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

def menu():
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

