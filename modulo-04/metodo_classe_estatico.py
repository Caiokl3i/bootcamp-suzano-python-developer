class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_data_nasc(cls, ano, nome):
        idade = 2022 - ano
        return cls(nome, idade)
    
    @staticmethod
    def maior_idade( idade):
        return idade <= 18


p2 = Pessoa.criar_de_data_nasc(2000, 12, 20, 'Caio')

print(Pessoa.maior_idade(18))
print(Pessoa.maior_idade(8))