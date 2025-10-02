from models.historico import Historico

class Conta:
    # metodo construtor
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente             # <-- associação com Cliente
        self._historico = Historico()     # <-- composição: Conta sempre tem um Histórico
    
    @property # uso do @property pra acessar como conta.saldo).
    def saldo(self):
        '''
        Método para pegar a propriedade e retornar a propriedade do tipo float
        '''
        return self._saldo
    
    @property 
    def numero(self):
        '''
        Método para pegar o numero e retorna o saldo do tipo float
        '''
        return self._numero
    
    @property 
    def agencia(self):
        '''
        Método para pegar a agencia e retorna o saldo do tipo float
        '''
        return self._agencia
    
    @property
    def cliente(self):
        '''
        Método para pegar o cliente e retorna o saldo do tipo float
        '''
        return self._cliente
    
    @property
    def historico(self):
        '''
        Método para pegar o historico e retorna o saldo do tipo float
        '''
        return self._historico
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        '''
        Método que cria uma nova conta e retorna uma instância da classe Conta
        '''
        return cls(numero, cliente)
    
    def sacar(self, valor):
        '''
        Método que realiza o saque do valor por parâmetro e retorna um booleano
        '''
        saldo = self.saldo
        excedeu_saldo = valor > saldo
        
        if excedeu_saldo:
            print('!! Operação falhou. Saldo insuficiente !!')
        elif valor > 0:
            self._saldo -= valor
            print('## Saque realizado com sucesso! ##')
            return True
        else:
            print('!! Operação falhou !!')
            
        return False
        
    def depositar(self, valor):
        '''
        Método para depositar o valor por parâmetro e retorna um booleano
        '''
        
        if valor > 0:
            self._saldo += valor
            print('!! Deposito realizado com sucesso !!')
            return True
        else:
            print('## Valor inválido ##')
            
        return False