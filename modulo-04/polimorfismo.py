"""
Polimorfismo em Python
----------------------

Polimorfismo = "muitas formas"
É a capacidade de um mesmo método ou operação assumir comportamentos diferentes,
dependendo do objeto que o utiliza.

Na prática:
- Diferentes classes podem ter métodos com o mesmo nome.
- O Python permite que esses métodos sejam chamados de forma uniforme,
  mesmo que cada classe os implemente de maneira diferente.
"""

# ===============================================================
# 1. Exemplo básico de polimorfismo
# ===============================================================

class Gato:
    def falar(self):
        return "Miau!"

class Cachorro:
    def falar(self):
        return "Au au!"

# Apesar de serem classes diferentes, ambas têm o método falar()
animais = [Gato(), Cachorro()]

for animal in animais:
    print(animal.falar())  # polimorfismo: mesmo método, diferentes formas


# ===============================================================
# 2. Polimorfismo com Herança
# ===============================================================
# - Uma classe base define um método genérico.
# - As classes filhas sobrescrevem esse método de acordo com sua necessidade.
# ===============================================================

class Animal:
    def falar(self):
        return "Som genérico de animal"

class Gato2(Animal):
    def falar(self):
        return "Miau!"

class Cachorro2(Animal):
    def falar(self):
        return "Au au!"

class Vaca(Animal):
    def falar(self):
        return "Muuu!"

animais2 = [Gato2(), Cachorro2(), Vaca()]

for animal in animais2:
    print(animal.falar())  # cada classe define sua própria versão


# ===============================================================
# 3. Funções polimórficas
# ===============================================================
# - O polimorfismo também aparece em funções que aceitam objetos
#   de tipos diferentes, contanto que tenham o mesmo "contrato" (método esperado).
# ===============================================================

def fazer_animal_falar(animal):
    print(animal.falar())

fazer_animal_falar(Gato2())
fazer_animal_falar(Cachorro2())
fazer_animal_falar(Vaca())


# ===============================================================
# 4. Exemplo prático: Sistema de Pagamentos
# ===============================================================
# - Um mesmo método (processar_pagamento) pode ser implementado
#   de várias formas, dependendo do tipo de pagamento.
# ===============================================================

class Pagamento:
    def processar_pagamento(self, valor):
        raise NotImplementedError("Esse método deve ser sobrescrito!")

class CartaoCredito(Pagamento):
    def processar_pagamento(self, valor):
        print(f"Pagamento de R${valor} processado no cartão de crédito.")

class Boleto(Pagamento):
    def processar_pagamento(self, valor):
        print(f"Boleto gerado no valor de R${valor}.")

class Pix(Pagamento):
    def processar_pagamento(self, valor):
        print(f"Transferência PIX de R${valor} realizada.")

pagamentos = [CartaoCredito(), Boleto(), Pix()]

for p in pagamentos:
    p.processar_pagamento(100)


# ===============================================================
# Conclusão:
# ===============================================================
# - Polimorfismo = diferentes objetos respondendo a mesma interface/método.
# - Pode ser usado sem herança (mesmo nome de método em classes distintas).
# - Com herança, é comum sobrescrever métodos da classe base.
# - Muito útil para escrever código flexível e genérico.
# ===============================================================

class Passaro:
    def voar(self):
        print('Voando...')

class Pardal(Passaro):
    def voar(self):
        super().voar()

class Avestruz(Passaro):
    def voar(self):
        print('Avestruz nao voa')

def plano_voo(obj):
    obj.voar()


p = Pardal()
a = Avestruz()

plano_voo(p)
plano_voo(a)