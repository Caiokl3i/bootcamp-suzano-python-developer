from datetime import datetime

class Historico:
    def __init__(self):
        self._transacao = []
    
    @property
    def transacoes(self):
        return self._transacao

    def adicionar_transacao(self, transacao):
        self._transacao.append(
            {
            'tipo': transacao.__class__.__name__,
            'valor': transacao.valor,
            'data': datetime.now()
            }
        )