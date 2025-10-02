from models import Cliente, ContaCorrente, Conta, Deposito, Historico, PessoaFisica, Saque, Transacao
import textwrap

def mostrar_menu():
    while True:
        print("\n============ SISTEMA BANCÁRIO ============")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Ver Extrato")
        print("4 - Nova conta")
        print("5 - Listar contas")
        print("6 - Novo usuário")
        print("0 - Sair")
        
        try:
            option = int(input('\nEscolha uma das opções acima: '))
        except ValueError:
            print("\nIsso não é um número válido!")
            continue
        
        if option < 0 or option > 7:
            print('\nNúmero inválido')
            continue
        
        return option

def depositar(clientes):
        cpf = input('Informe o CPF:')
        cliente = filtrar_cliente(cpf, clientes)
        
        if not cliente:
            print('!! Cliente Não encontrado !!')
            return
        
        valor = float(input('Informe o valor do deposito:'))
        transacao = Deposito(valor)
        
        conta = recuperar_conta_cliente(cliente)
        if not conta:
            return
        
        cliente.realizar_transacao(conta, transacao)
        
def sacar(clientes):
    cpf = input('informe o cpf do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print('!! Cliente não encontrado !!')
        return
    
    valor = float(input('Informe o valor do saqueÇ '))
    transacao = Saque(valor)
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    cpf = input('informe o cpf do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print('!! Cliente não encontrado !!')
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    print('\n=============== EXTRATO ===============\n')
    transacoes = conta.historico.transacoes
    
    extrato = ''
    if not transacoes:
        extrato = 'Não foram encontradas movimentações'
    else:
        for transacao in transacoes:
            extrato += f'\n{transacao["tipo"]}: \n\tR${transacao["valor"]:.2f}'
    
    print(extrato)
    print(f'\nSaldo:\n\tR$ {conta.saldo:.2f}')
    
    print('\n=======================================\n')
    
def criar_cliente(clientes):
    cpf = input('informe o cpf (apenas números): ')
    cliente = filtrar_cliente(cpf, clientes)
    
    if cliente:
        print('!! Já existe um cliente com esse CPF !!')
        return
    
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd/mm/aaaa): ')
    endereco = input('Informe o endereço: ')
    
    cliente = PessoaFisica(cpf, nome, data_nascimento, endereco)
    clientes.append(cliente)
    
    print('!! Cadastro feito com sucesso !!')
    
def criar_conta(numero_conta, clientes, contas):
    cpf = input('informe o cpf do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print('!! Cliente não encontrado !!')
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print('\n ## Conta criada com sucesso ##')
    
def listar_contas(contas):
    print('================= CONTAS =================')
    for conta in contas:
        print(textwrap.dedent(str(conta)))
    print('===========================================')

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print('!! Cliente não possui conta !!')
        return
    
    return cliente.contas[0]