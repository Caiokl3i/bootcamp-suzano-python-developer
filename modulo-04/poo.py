"""
Anotações de Programação Orientada a Objetos (POO) em Python
------------------------------------------------------------

POO é um paradigma de programação baseado em "objetos", que combinam
dados (atributos) e comportamentos (métodos).

Pilares da POO:
1. Abstração
2. Encapsulamento
3. Herança
4. Polimorfismo
"""

# ------------------------------------------------------------
# CLASSES E OBJETOS
# ------------------------------------------------------------

# Classe: "molde" para criar objetos
class Pessoa:
    def __init__(self, nome, idade):  # Método construtor
        self.nome = nome
        self.idade = idade

    def apresentar(self):  # Método da classe
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")


# Criando um objeto (instância da classe)
p1 = Pessoa("Caio", 19)
p1.apresentar()


# ------------------------------------------------------------
# ENCAPSULAMENTO
# ------------------------------------------------------------

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo  # Atributo "privado"

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente.")

    def ver_saldo(self):
        return self.__saldo


conta = ContaBancaria("Caio", 1000)
conta.depositar(500)
print(conta.ver_saldo())


# ------------------------------------------------------------
# HERANÇA
# ------------------------------------------------------------

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print("Som genérico de animal.")


class Cachorro(Animal):  # Herda de Animal
    def falar(self):
        print("Au au!")


class Gato(Animal):  # Herda de Animal
    def falar(self):
        print("Miau!")


dog = Cachorro("Rex")
cat = Gato("Mimi")

dog.falar()
cat.falar()


# ------------------------------------------------------------
# POLIMORFISMO
# ------------------------------------------------------------

animais = [Cachorro("Rex"), Gato("Mimi")]

for animal in animais:
    animal.falar()  # Cada objeto responde de forma diferente


# ------------------------------------------------------------
# CLASSES ABSTRATAS (com abc)
# ------------------------------------------------------------
from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def mover(self):
        pass


class Carro(Veiculo):
    def mover(self):
        print("O carro está andando.")


class Barco(Veiculo):
    def mover(self):
        print("O barco está navegando.")


meu_carro = Carro()
meu_barco = Barco()

meu_carro.mover()
meu_barco.mover()