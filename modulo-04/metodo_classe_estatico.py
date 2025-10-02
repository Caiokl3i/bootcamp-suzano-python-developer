class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    # O @classmethod é usado quando você quer criar (ou manipular) uma instância
    # da própria classe dentro do método, sem precisar de uma instância já existente.
    # Ele funciona como uma “fábrica” que sabe criar objetos da classe.
    def criar_de_data_nasc(cls, ano, nome):
        idade = 2022 - ano
        return cls(nome, idade)
    
    @staticmethod
    def maior_idade( idade):
        return idade <= 18


p2 = Pessoa.criar_de_data_nasc(2000, 12, 20, 'Caio')

print(Pessoa.maior_idade(18))
print(Pessoa.maior_idade(8))