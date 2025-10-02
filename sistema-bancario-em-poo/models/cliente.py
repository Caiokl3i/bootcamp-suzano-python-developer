class Cliente():
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
    
    def realizar_transacao(self, conta, transacao):
        '''
        Realiza uma transacao, pode ser saque ou deposito, 
        '''
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        '''
        Vincula uma conta ao cliente
        '''
        self.contas.append(conta)