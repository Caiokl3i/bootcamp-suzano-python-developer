# Funções são blocos de código reutilizáveis que executam uma tarefa específica.
# Elas ajudam a organizar o código, evitar repetição e melhorar a legibilidade.

# -------------------------------
# 1. Definindo Funções
# -------------------------------
# Para criar uma função, usamos a palavra-chave 'def', seguida do nome da função e parênteses.
# O código da função deve estar indentado (geralmente 4 espaços).

def saudacao():
    print("Olá! Seja bem-vindo.")

saudacao()  # Chamando a função

# -------------------------------
# 2. Funções com Parâmetros
# -------------------------------
# Parâmetros são variáveis que a função recebe para usar internamente.
# Eles permitem personalizar a execução da função.

def saudacao_nome(nome):
    print(f"Olá, {nome}! Seja bem-vindo.")

saudacao_nome("Caio")

# -------------------------------
# 3. Funções com Retorno
# -------------------------------
# O comando 'return' permite que a função devolva um valor para quem a chamou.

def soma(a, b):
    return a + b

resultado = soma(5, 7)
print("Resultado da soma:", resultado)

# -------------------------------
# 4. Parâmetros Padrão
# -------------------------------
# Podemos definir valores padrão para parâmetros, que serão usados caso não sejam passados valores.

def saudacao_personalizada(nome="Visitante"):
    print(f"Olá, {nome}!")

saudacao_personalizada()       # Usa o padrão
saudacao_personalizada("Ana")  # Substitui o padrão

# -------------------------------
# 5. Argumentos Nomeados
# -------------------------------
# Podemos chamar funções especificando o nome do parâmetro, deixando a ordem flexível.

def informacoes_pessoa(nome, idade, cidade):
    print(f"{nome} tem {idade} anos e mora em {cidade}.")

informacoes_pessoa(idade=20, nome="Caio", cidade="Campo Grande")

# -------------------------------
# 6. Funções Anônimas (Lambda)
# -------------------------------
# Funções pequenas podem ser criadas com 'lambda', sem precisar do 'def'.

multiplicar = lambda x, y: x * y
print("Multiplicação:", multiplicar(3, 4))

# -------------------------------
# 7. Escopo de Variáveis
# -------------------------------
# Variáveis definidas dentro de funções são locais (existem apenas lá dentro).
# Variáveis fora de funções são globais.

variavel_global = "Sou global"

def mostrar_escopo():
    variavel_local = "Sou local"
    print(variavel_local)
    print(variavel_global)  # Global pode ser acessada dentro da função

mostrar_escopo()
# print(variavel_local)  # ERRO: variavel_local não existe fora da função

# -------------------------------
# 8. Docstrings
# -------------------------------
# Docstrings são strings de documentação de funções, usadas para explicar o que a função faz.

def soma_documentada(a, b):
    """
    Esta função recebe dois números (a e b) e retorna a soma deles.
    """
    return a + b

print(soma_documentada.__doc__)  # Mostra a docstring da função

# -------------------------------
# 9. Retorno Múltiplo
# -------------------------------
# Podemos retornar múltiplos valores usando tuplas

def operacoes(a, b):
    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    divisao = a / b
    return soma, subtracao, multiplicacao, divisao

s, sub, mult, div = operacoes(10, 2)
print(s, sub, mult, div)

# -------------------------------
# 10. Funções como Objetos
# -------------------------------
# Funções podem ser atribuídas a variáveis ou passadas como argumentos

def dobrar(x):
    return x * 2

def aplicar_funcao(func, valor):
    return func(valor)

print(aplicar_funcao(dobrar, 5))  # Chama dobrar(5) através de outra função

# -------------------------------
# 11. Funções Recursivas
# -------------------------------
# Uma função pode se chamar a si mesma, útil para problemas como fatorial ou Fibonacci

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

print("Fatorial de 5:", fatorial(5))
