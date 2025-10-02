from models.conta import Conta
from models.saque import Saque

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
    
    def sacar(self, valor):
        qtde_saques = len([transacao for transacao in self.historico.transacoes
                                if transacao["tipo"] == Saque.__name__] # == 'saque'
            )
        
        excedeu_limite = valor > self.limite
        excedeu_saques = qtde_saques > self.limite_saques
        
        if excedeu_limite:
            print('!! Operação falhou. O valor do saque excede o limite de saque de R$500,00 !!')
            
        elif excedeu_saques:
            print('!! Operação falhou. O valor do saque excedeu o limite diario')
            
        else:
            return super().sacar(valor)
        return False
    
    def __str__(self):
        return f'Agencia:\t{self.agencia}\nC/C:\t\t{self.numero}\nTitular:\t{self.cliente.nome}'
    