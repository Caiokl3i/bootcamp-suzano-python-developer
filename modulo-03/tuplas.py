# ===========================================
# TUPLAS EM PYTHON
# ===========================================

# Tupla é uma estrutura de dados parecida com a lista,
# mas com uma diferença fundamental:
# -> Tuplas são IMUTÁVEIS (não podem ser alteradas após criadas).

# Criando tuplas
tupla1 = (1, 2, 3, 4)
print(tupla1)

# Tupla também pode ter tipos diferentes
tupla2 = ("texto", 10, 3.14, True)
print(tupla2)

# Tupla com um único elemento precisa da vírgula no final
um_elemento = (5,)
print(type(um_elemento))  # <class 'tuple'>

# Tuplas podem ser criadas sem parênteses (Python reconhece automaticamente)
tupla3 = 1, 2, 3
print(tupla3)

# --------------------------------------------------------------------
# ACESSO A ELEMENTOS

print(tupla1[0])   # primeiro elemento -> 1
print(tupla1[-1])  # último elemento -> 4
print(tupla1[1:3]) # slicing -> (2, 3)

# ----------------------------------------------------------------
# ITERANDO SOBRE TUPLAS

for item in tupla2:
    print(item)

# -----------------------------------------------------------------
# MÉTODOS DISPONÍVEIS EM TUPLAS

# count(valor) -> conta quantas vezes o valor aparece
print(tupla1.count(2))  # 1

# index(valor) -> retorna a primeira posição do valor
print(tupla1.index(3))  # índice 2

# ------------------------------------------------------------------
# DESEMPACOTAMENTO DE TUPLAS

coordenadas = (10, 20)
x, y = coordenadas  # cada variável recebe um valor
print("x:", x, "y:", y)

# Pode usar underline (_) para ignorar valores
tupla4 = (1, 2, 3)
a, _, c = tupla4
print(a, c)

# -----------------------------------------------------------------
# TUPLAS DENTRO DE LISTAS E VICE-VERSA

lista_de_tuplas = [(1, 2), (3, 4), (5, 6)]
print(lista_de_tuplas[1][0])  # acessa 3

tupla_de_listas = ([1, 2], [3, 4])
print(tupla_de_listas)

# Obs: elementos MUTÁVEIS dentro da tupla (como listas) podem ser alterados!
tupla_de_listas[0].append(99)
print(tupla_de_listas)

# -----------------------------------------------------------------
# CONVERSÃO ENTRE LISTA E TUPLA

lista = [1, 2, 3]
tupla = tuple(lista)   # converte lista em tupla
print(tupla)

nova_lista = list(tupla)  # converte tupla em lista
nova_lista.append(4)
print(nova_lista)

# ------------------------------------------------------------------
# USOS COMUNS DE TUPLAS

# 1. Armazenar dados imutáveis
cores = ("vermelho", "verde", "azul")

# 2. Retornar múltiplos valores de uma função
def dividir(a, b):
    quociente = a // b
    resto = a % b
    return quociente, resto  # retorna tupla

resultado = dividir(10, 3)
print(resultado)      # (3, 1)
print(resultado[0])   # quociente
print(resultado[1])   # resto

# 3. Uso como chave em dicionários (tupla é hashable, lista não é)
dicionario = {
    (0,0): "origem",
    (1,2): "ponto A",
}
print(dicionario[(1,2)])