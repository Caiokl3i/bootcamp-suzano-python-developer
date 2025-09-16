# conhecendo_a_linguagem.py
# Resumo básico de Python

# Tipos de dados
inteiro = 10          # número inteiro
decimal = 3.14        # número decimal
texto = "Olá, Python" # texto
booleano = True       # verdadeiro/falso
lista = [1, 2, 3]     # lista
tupla = (4, 5, 6)     # tupla
dicionario = {"a": 1, "b": 2}  # dicionário

print(inteiro, decimal, texto, booleano)
print(lista, tupla, dicionario)

# Modo interativo
# permite testar código rápido no console
# ex: x = 5, x + 2 → 7

# Variáveis e constantes
nome = "Caio"
idade = 19
PI = 3.14159  # constante

print("Nome:", nome)
print("Idade:", idade)
print("Constante PI:", PI)

# Conversão de tipos
num_str = "123"
num_int = int(num_str)      
num_float = float(num_str)  
texto = str(num_int)        

print(num_int, num_float, texto)

# Entrada e saída de dados
# input() recebe dados do usuário
# print() mostra dados na tela

# Exemplo de saída formatada
idade_usuario = 20
print(f"Você tem {idade_usuario} anos")