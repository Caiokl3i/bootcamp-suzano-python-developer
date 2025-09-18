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
import functions as func

depositos_extrato = []
saques_extrato = []
carteira = 0

limite_operacoes = 10
operacoes_diarias = 0

dia_atual = date.today()

while True:
    option = func.mostrar_menu(dia_atual, limite_operacoes, operacoes_diarias)

    match option:
        case 1:
            carteira, depositos_extrato, operacoes_diarias = func.realizar_deposito(carteira, depositos_extrato, operacoes_diarias, limite_operacoes)
        case 2:
            carteira, saques_extrato, operacoes_diarias = func.realizar_saque(carteira, saques_extrato, operacoes_diarias, limite_operacoes)
        case 3:
            func.consultar_extrato(depositos_extrato, saques_extrato, carteira)
        case 4:
            dia_atual, operacoes_diarias = func.aumentar_dia(dia_atual, operacoes_diarias)
        case 0:
            print('\nSaindo ...')
            break
