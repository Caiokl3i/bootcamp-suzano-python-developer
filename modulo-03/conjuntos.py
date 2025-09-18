# CONJUNTOS (set) EM PYTHON

# Um conjunto (set) é uma coleção NÃO ORDENADA e SEM ELEMENTOS DUPLICADOS.
# É inspirado na matemática (teoria dos conjuntos).

# Criando conjuntos
conjunto1 = {1, 2, 3, 4}
print(conjunto1)

# Conjunto ignora duplicados
conjunto2 = {1, 2, 2, 3, 4, 4}
print(conjunto2)  # {1, 2, 3, 4}

# Criando conjunto a partir de lista
lista = [1, 2, 2, 3, 3, 4]
conjunto3 = set(lista)
print(conjunto3)  # {1, 2, 3, 4}

# Criando conjunto vazio
conjunto_vazio = set()
print(type(conjunto_vazio))  # <class 'set'>

# -------------------------------------------
# OPERAÇÕES DE CONJUNTOS
# -------------------------------------------

A = {1, 2, 3}
B = {3, 4, 5}

# União (todos os elementos sem repetir)
print(A | B)  # {1, 2, 3, 4, 5}
print(A.union(B))

# Interseção (apenas os que aparecem em ambos)
print(A & B)  # {3}
print(A.intersection(B))

# Diferença (o que tem em A mas não em B)
print(A - B)  # {1, 2}
print(A.difference(B))

# Diferença simétrica (elementos exclusivos de cada conjunto)
print(A ^ B)  # {1, 2, 4, 5}
print(A.symmetric_difference(B))

# -------------------------------------------
# MÉTODOS PRINCIPAIS
# -------------------------------------------

numeros = {1, 2, 3}

# Adicionar elementos
numeros.add(4)
print(numeros)

# Atualizar com múltiplos elementos
numeros.update([5, 6, 7])
print(numeros)

# Remover elementos
numeros.remove(7)   # erro se não existir
print(numeros)

numeros.discard(99) # não gera erro se não existir
print(numeros)

# Remover e retornar um elemento aleatório
valor = numeros.pop()
print("Removido:", valor, "Restante:", numeros)

# Limpar conjunto
numeros.clear()
print(numeros)  # set()

# -------------------------------------------
# TESTES DE PERTINÊNCIA
# -------------------------------------------
animais = {"cachorro", "gato", "coelho"}
print("gato" in animais)    # True
print("lobo" not in animais) # True

# -------------------------------------------
# SUBCONJUNTO E SUPERCONJUNTO
# -------------------------------------------
X = {1, 2}
Y = {1, 2, 3, 4}

print(X.issubset(Y))     # True -> X está contido em Y
print(Y.issuperset(X))   # True -> Y contém X

# Conjuntos disjuntos (sem interseção)
Z = {5, 6}
print(X.isdisjoint(Z))   # True

# -------------------------------------------
# FROZENSET (conjunto imutável)
# -------------------------------------------
# É uma versão imutável de set, pode ser usado como chave em dicionários.
frozen = frozenset([1, 2, 3])
print(frozen)

# frozen.add(4)  # ERRO -> não é possível modificar

