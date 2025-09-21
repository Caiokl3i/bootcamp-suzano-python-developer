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
import functions as func
import time

depositos_extrato = []
saques_extrato = []
carteira = 0

limite_operacoes = 10
operacoes_diarias = 0

dia_atual = datetime.now()


while True:
    time.sleep(1)
    option = func.mostrar_menu(dia_atual, limite_operacoes, operacoes_diarias)

    match option:
        case 1:
            carteira, depositos_extrato, operacoes_diarias = func.realizar_deposito(carteira, depositos_extrato, operacoes_diarias, limite_operacoes, dia_atual)
        case 2:
            carteira, saques_extrato, operacoes_diarias = func.realizar_saque(carteira, saques_extrato, operacoes_diarias, limite_operacoes, dia_atual)
        case 3:
            func.consultar_extrato(depositos_extrato, saques_extrato, carteira)
        case 4:
            dia_atual, operacoes_diarias = func.aumentar_dia(dia_atual, operacoes_diarias)
        case 0:
            print('\nSaindo ...')
            break
