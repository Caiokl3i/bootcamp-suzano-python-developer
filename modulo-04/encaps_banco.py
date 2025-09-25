class Conta():
    def __init__(self, n_agencia, saldo=0):
        self._saldo = saldo
        self.n_agencia = n_agencia

    def depositar(self, valor):
        # ...
        self.valor += valor
    
    def sacar(self, valor):
        # ...
        self.valor -= valor

    def mostrar_saldo(self):
        return self._saldo
    
    
conta = Conta('0001', 100)
print(conta.n_agencia)
print(conta.mostrar_saldo())