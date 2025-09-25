class Bicicleta(object):
    def __init__(self, cor, modelo, ano, valor): # função contrutora
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        

    def buzinar(self):
        print('Bi Bi buzinando')
    
    def correr(self):
        print('Correndo')
    
    def parar(self):
        print('Parando')
        print('Bicicleta parada')
    
    # def __str__(self):
    #     return f'Bicicleta: {self.ano}, {self.modelo}, {self.valor}, {self.cor}'
    
    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}' 
    
bi1 = Bicicleta('vermelha', 'caloy', 2024, 1200)

bi1.buzinar()
bi1.correr()
bi1.parar()

print(bi1.ano)
print(bi1.modelo)
print(bi1.cor)
print(bi1.valor)

bi2 = Bicicleta('verde', 'monark', 2022, 1000)

print(bi2)
print(bi1)

