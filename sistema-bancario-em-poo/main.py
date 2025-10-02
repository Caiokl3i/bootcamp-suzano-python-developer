import functions as func
import time

clientes = []
contas = []

while True:
    time.sleep(1)
    option = func.mostrar_menu()

    match option:
        case 1:
            func.depositar(clientes)
        case 2:
            func.sacar(clientes)
        case 3:
            func.exibir_extrato(clientes)
        case 4:
            numero_conta = len(contas) + 1
            func.criar_conta(numero_conta, clientes, contas)
        case 5:
            func.listar_contas(contas)
        case 6:
            func.criar_cliente(clientes)
        case 0:
            print('\nSaindo ...')
            break
