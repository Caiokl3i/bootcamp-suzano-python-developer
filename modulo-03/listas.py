# Introdução às Listas em Python

# Lista é uma estrutura de dados que pode armazenar múltiplos valores
# dentro de uma única variável. É MUTÁVEL, ou seja, pode ser alterada.

# Exemplo de lista
frutas = ["maçã", "banana", "laranja"]
print(frutas)

# Listas podem conter tipos diferentes
mistura = [10, "texto", True, 3.14]
print(mistura)

# Listas podem estar vazias
vazia = []
print(vazia)

# Vantagens:
# - Armazenar vários valores em uma só variável
# - Fácil manipulação com métodos prontos

# ====================================================================

# Criação de listas e acesso aos dados

# Criando listas
numeros = [1, 2, 3, 4, 5]

# Acessando elementos (índice começa em 0)
print(numeros[0])   # primeiro elemento -> 1
print(numeros[2])   # terceiro elemento -> 3

# Índices negativos contam de trás para frente
print(numeros[-1])  # último -> 5
print(numeros[-2])  # penúltimo -> 4

# FATIAS (slicing)
print(numeros[1:4])  # do índice 1 até o 3 -> [2, 3, 4]
print(numeros[:3])   # do início até o índice 2 -> [1, 2, 3]
print(numeros[2:])   # do índice 2 até o fim -> [3, 4, 5]

# Alterando valores
numeros[0] = 100
print(numeros)  # [100, 2, 3, 4, 5]

# Listas podem armazenar listas (listas aninhadas)
matriz = [[1, 2], [3, 4]]
print(matriz[0][1])  # acessa 2

# =================================================================================

# Métodos da classe list

# Criando uma lista base
frutas = ["maçã", "banana", "laranja"]

# Adicionar elementos
frutas.append("uva")        # adiciona no final
print(frutas)

frutas.insert(1, "abacaxi") # insere na posição 1
print(frutas)

# Remover elementos
frutas.remove("banana")     # remove a primeira ocorrência
print(frutas)

ultimo = frutas.pop()       # remove o último (ou por índice)
print(ultimo, frutas)

# Contar e localizar
print(frutas.count("maçã"))  # conta ocorrências
print(frutas.index("laranja"))  # índice do valor

# Ordenar
numeros = [5, 2, 8, 1]
numeros.sort()          # ordena crescente
print(numeros)

numeros.sort(reverse=True)  # ordena decrescente
print(numeros)

# Copiar listas
copia = frutas.copy()
print(copia)

# Juntar listas
mais_frutas = ["kiwi", "manga"]
frutas.extend(mais_frutas)
print(frutas)

# Limpar lista
frutas.clear()
print(frutas)

numeros = [n**2 if n > 6 else n for n in range(10) if n % 2 == 0] 
print(numeros)