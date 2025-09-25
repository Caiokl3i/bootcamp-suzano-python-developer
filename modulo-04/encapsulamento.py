"""
Encapsulamento em Python
------------------------

O encapsulamento é um dos pilares da Programação Orientada a Objetos (POO).
Ele significa "esconder os detalhes internos" de uma classe e controlar
como os atributos e métodos podem ser acessados.

Em Python, não existe encapsulamento rígido como em Java ou C++,
mas existem convenções que usamos para indicar o nível de acesso.
"""

# ===============================================================
# 1. Atributos Públicos
# ===============================================================
# - Podem ser acessados diretamente de qualquer lugar.
# - NÃO têm underscore no nome.
# ===============================================================

class Pessoa:
    def __init__(self, nome):
        self.nome = nome  # público

p1 = Pessoa("Caio")
print(p1.nome)  # acesso direto (ok)


# ===============================================================
# 2. Atributos Protegidos
# ===============================================================
# - Usam um underscore na frente: _atributo
# - Indicam que NÃO devem ser acessados diretamente fora da classe,
#   mas ainda podem ser acessados (apenas uma convenção).
# ===============================================================

class Pessoa2:
    def __init__(self, nome):
        self._nome = nome  # protegido

p2 = Pessoa2("Ana")
print(p2._nome)  # tecnicamente funciona, mas "não é recomendado"


# ===============================================================
# 3. Atributos Privados
# ===============================================================
# - Usam dois underscores: __atributo
# - Ativam o "name mangling": o Python renomeia o atributo
#   internamente para _NomeDaClasse__atributo.
# - Isso dificulta (mas não impede) o acesso direto.
# ===============================================================

class Pessoa3:
    def __init__(self, nome):
        self.__nome = nome  # privado

    def mostrar_nome(self):
        return self.__nome  # acesso controlado por método

p3 = Pessoa3("Victor")
print(p3.mostrar_nome())  # acesso permitido pelo método

# print(p3.__nome)  # ERRO: não pode acessar diretamente
print(p3._Pessoa3__nome)  # "jeitinho" para acessar (não recomendado)


# ===============================================================
# 4. Exemplo Completo: Conta Bancária
# ===============================================================
# - O saldo é privado.
# - O acesso e as alterações são feitos apenas por métodos.
# - Isso evita que alguém altere o saldo de forma incorreta.
# ===============================================================

class ContaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  # privado

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente")

    def mostrar_saldo(self):
        return self.__saldo

conta = ContaBancaria(1000)
conta.depositar(500)
conta.sacar(200)
print("Saldo:", conta.mostrar_saldo())

# conta.__saldo  # ERRO: não acessa direto
# conta._ContaBancaria__saldo  # "jeitinho" (não recomendado)


# ===============================================================
# Conclusão:
# ===============================================================
# - Encapsulamento = proteger os dados internos de uma classe.
# - Público: acesso liberado.
# - Protegido (_): "aviso" para não acessar fora da classe.
# - Privado (__): renomeia internamente para dificultar acesso.
# - Em Python, usamos principalmente convenções e métodos getters/setters
#   para garantir segurança e clareza no código.
# ===============================================================
