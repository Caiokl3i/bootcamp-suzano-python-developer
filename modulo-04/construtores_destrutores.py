class Cachorro():
    def __init__(self, nome, cor, acordado = True):
        print('inicializando a classe')
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def __del__(self):
        print('Removendo a instancia da classe')
    
    def falar(self):
        print('Au Au')



c = Cachorro('Rex', 'Marron', False)
print(c.nome)

del c