class Veiculo():
    def __init__(self, cor, placa, num_rodas):
        self.cor = cor
        self.placa = placa
        self.num_rodas = num_rodas
    
    def ligar_motor(self):
        print('Ligando o motor')
    
    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}' 
    
    
class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, num_rodas, carregado):
        super().__init__(cor, placa, num_rodas)
        self.carregado = carregado
    
    def esta_carregado(self):
        print(f'{'Estou carregado' if self.carregado else 'Não estou carregado'}')


moto = Motocicleta('preta', 'ABC-1234', 2)

moto.ligar_motor()
print(moto)

carro = Carro('branco', 'SDA-3456', 4)

carro.ligar_motor()
print(carro)

caminhao = Caminhao('azul', 'JKL-3224', 6, False)

print(caminhao.cor)
caminhao.esta_carregado()
print(caminhao)