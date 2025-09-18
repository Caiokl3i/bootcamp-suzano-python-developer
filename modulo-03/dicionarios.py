# DICIONÁRIOS EM PYTHON

# Dicionário (dict) é uma coleção de pares "chave: valor"
# -> As chaves são ÚNICAS e imutáveis (strings, números, tuplas, etc.)
# -> Os valores podem ser de qualquer tipo

# -------------------------------------------
# CRIAÇÃO DE DICIONÁRIOS
# -------------------------------------------

# Forma comum
pessoa = {
    "nome": "Caio",
    "idade": 19,
    "cidade": "Campo Grande"
}
print(pessoa)

# Criando com dict()
carro = dict(marca="Ford", modelo="Ka", ano=2015)
print(carro)

# Dicionário vazio
vazio = {}
print(vazio)

# -------------------------------------------
# ACESSANDO DADOS
# -------------------------------------------

print(pessoa["nome"])   # acesso por chave
print(pessoa.get("idade"))  # acesso seguro (não dá erro se não existir)

# Evita erro usando get()
print(pessoa.get("altura", "Não informado"))

# Alterando valores
pessoa["idade"] = 20
print(pessoa)

# Adicionando nova chave
pessoa["profissão"] = "Programador"
print(pessoa)

# -------------------------------------------
# ITERANDO EM DICIONÁRIOS
# -------------------------------------------

for chave in pessoa:
    print(chave, "->", pessoa[chave])

for chave, valor in pessoa.items():
    print(chave, ":", valor)

# Apenas chaves
print(list(pessoa.keys()))

# Apenas valores
print(list(pessoa.values()))

# -------------------------------------------
# MÉTODOS DA CLASSE DICT
# -------------------------------------------

dados = {"a": 1, "b": 2, "c": 3}

# .keys() -> retorna todas as chaves
print(dados.keys())

# .values() -> retorna todos os valores
print(dados.values())

# .items() -> retorna pares (chave, valor)
print(dados.items())

# .get(chave, valor_padrao)
print(dados.get("a"))         # 1
print(dados.get("z", "N/A"))  # N/A

# .update() -> atualiza valores ou adiciona novos pares
dados.update({"d": 4, "a": 100})
print(dados)

# .pop(chave) -> remove e retorna o valor
removido = dados.pop("b")
print(removido, dados)

# .popitem() -> remove o último par
print(dados.popitem())

# .setdefault(chave, valor) -> retorna valor se existir, senão cria
print(dados.setdefault("e", 5))
print(dados)

# .clear() -> esvazia o dicionário
dados.clear()
print(dados)

# -------------------------------------------
# USOS COMUNS DE DICIONÁRIOS
# -------------------------------------------

# 1. Representar entidades (tipo "objetos")
aluno = {"nome": "Ana", "curso": "ADS", "nota": 9.5}

# 2. Contagem de elementos
texto = "banana"
contador = {}
for letra in texto:
    contador[letra] = contador.get(letra, 0) + 1
print(contador)  # {'b':1, 'a':3, 'n':2}

# 3. Dicionário com tupla como chave (mapear coordenadas, por exemplo)
mapa = {
    (0, 0): "início",
    (1, 2): "ponto A",
    (2, 3): "ponto B"
}
print(mapa[(1,2)])
