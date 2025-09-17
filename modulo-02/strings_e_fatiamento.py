# Métodos úteis para strings em Python

texto = "  Olá, Python!  "

# -----------------
# Básicos
print(len(texto))        # tamanho da string
print(texto.strip())     # remove espaços extras
print(texto.lower())     # tudo minúsculo
print(texto.upper())     # tudo maiúsculo
print(texto.capitalize()) # primeira letra maiúscula
print(texto.title())     # primeira letra de cada palavra

# -----------------
# Busca
print(texto.find("Python"))   # posição da palavra (ou -1 se não achar)
print(texto.startswith("Olá")) # começa com?
print(texto.endswith("!"))     # termina com?
print("Python" in texto)       # contém?
print("Java" not in texto)     # não contém?

# -----------------
# Substituição
print(texto.replace("Python", "Mundo"))  # troca palavra

# -----------------
# Quebrar e juntar
print(texto.split(","))     # divide pelo separador
palavras = ["Python", "é", "legal"]
print(" ".join(palavras))   # junta com espaço

# -----------------
# Verificações
print("123".isdigit())    # só dígitos?
print("abc".isalpha())    # só letras?
print("abc123".isalnum()) # letras e números?
print("python".islower()) # tudo minúsculo?
print("PY".isupper())     # tudo maiúsculo?

# -----------------
# Formatação
nome = "Caio"
idade = 19
print("Nome: {}, Idade: {}".format(nome, idade))  # format()
print(f"Nome: {nome}, Idade: {idade}")            # f-string

# -------------------------------------------------------------------------

# Formas de interpolar strings em Python

nome = "Caio"
idade = 19

# -----------------
# f-string (mais usado, desde Python 3.6)
print(f"Meu nome é {nome} e tenho {idade} anos")

# -----------------
# format()
print("Meu nome é {} e tenho {} anos".format(nome, idade))
print("Meu nome é {0} e tenho {1} anos".format(nome, idade))  # por posição
print("Meu nome é {n} e tenho {i} anos".format(n=nome, i=idade))  # por nome

# -----------------
# % (estilo antigo, ainda funciona)
print("Meu nome é %s e tenho %d anos" % (nome, idade))
# %s = string, %d = inteiro, %f = float

# -----------------
# Template Strings (menos comum, precisa importar)
from string import Template

t = Template("Meu nome é $nome e tenho $idade anos")
print(t.substitute(nome=nome, idade=idade))

# -----------------------------------------------------------------------

# Fatiamento de strings em Python

texto = "Python"

# [inicio:fim:passo]
print(texto[0:3])   # Pyt (do 0 até antes do 3)
print(texto[:4])    # Pyth (do início até antes do 4)
print(texto[2:])    # thon (do 2 até o fim)
print(texto[-1])    # n (último caractere)
print(texto[-3:])   # hon (últimos 3)
print(texto[::2])   # Pto (de 2 em 2)
print(texto[::-1])  # nohtyP (invertido)

# usando slice() (equivalente ao [])
parte = slice(0, 4)     # do índice 0 até antes do 4
print(texto[parte])     # Pyth

# -------------------------------------------------------------------------

# Strings de Múltiplas Linhas

# Em Python, podemos criar strings que ocupam mais de uma linha
# usando três aspas simples ''' ou três aspas duplas """.

# Exemplo com três aspas duplas
texto1 = """Esta é uma string
que ocupa várias linhas.
Podemos escrever quantas linhas quisermos."""

print(texto1)
print("-------------------")

# Exemplo com três aspas simples
texto2 = '''Outra forma de criar
uma string de múltiplas linhas.
Funciona da mesma maneira que as aspas duplas.'''

print(texto2)
print("-------------------")

# Strings de múltiplas linhas preservam quebras de linha automaticamente
# Ou seja, o \n não é necessário, mas ainda pode ser usado se quisermos adicionar linhas extras
texto3 = """Linha 1
Linha 2
Linha 3\nLinha 4 com \nquebra manual"""

print(texto3)

# Também podemos usar strings de múltiplas linhas para documentar funções ou classes (docstrings)
def exemplo():
    """
    Esta função é um exemplo de docstring.
    Docstrings servem para documentar funções, métodos ou classes.
    """
    pass