# operadores_basico.py
# Resumo básico sobre operadores em Python


# Operadores Aritméticos

# Realizam cálculos matemáticos
a = 10
b = 3

soma = a + b        # adição
subtracao = a - b   # subtração
multiplicacao = a * b # multiplicação
divisao = a / b     # divisão (resultado float)
divisao_inteira = a // b # divisão inteira
resto = a % b       # resto da divisão
potencia = a ** b   # exponenciação

print("Aritméticos:", soma, subtracao, multiplicacao, divisao, divisao_inteira, resto, potencia)


# Operadores de Comparação

# Comparam valores e retornam True ou False
print("Comparação:")
print(a == b)  # igual
print(a != b)  # diferente
print(a > b)   # maior
print(a < b)   # menor
print(a >= b)  # maior ou igual
print(a <= b)  # menor ou igual


# Operadores de Atribuição

# Atribuem valores às variáveis, podendo combinar com operações
x = 5
x += 2   # x = x + 2
x -= 1   # x = x - 1
x *= 3   # x = x * 3
x /= 2   # x = x / 2
x %= 2   # x = x % 2

print("Atribuição:", x)


# Operadores Lógicos

# Usados para combinar condições
v = True
f = False

print("Lógicos:")
print(v and f)  # AND: True se ambos True
print(v or f)   # OR: True se pelo menos um True
print(not v)    # NOT: inverte o valor


# Operadores de Identidade

# Verificam se duas variáveis são o mesmo objeto
y = [1, 2, 3]
z = y
w = [1, 2, 3]

print("Identidade:")
print(y is z)  # True, mesmo objeto
print(y is w)  # False, objetos diferentes
print(y is not w) # True


# Operadores de Associação

# Verificam se um valor está contido em uma coleção
lista = [1, 2, 3, 4]

print("Associação:")
print(2 in lista)    # True
print(5 not in lista) # True
